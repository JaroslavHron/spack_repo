##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import os
import sys

# Trilinos is complicated to build, as an inspiration a couple of links to
# other repositories which build it:
# https://github.com/hpcugent/easybuild-easyblocks/blob/master/easybuild/easyblocks/t/trilinos.py#L111
# https://github.com/koecher/candi/blob/master/deal.II-toolchain/packages/trilinos.package
# https://gitlab.com/configurations/cluster-config/blob/master/trilinos.sh
# https://github.com/Homebrew/homebrew-science/blob/master/trilinos.rb and some
# relevant documentation/examples:
# https://github.com/trilinos/Trilinos/issues/175


class Trilinos(Package):
    """The Trilinos Project is an effort to develop algorithms and enabling
    technologies within an object-oriented software framework for the solution
    of large-scale, complex multi-physics engineering and scientific problems.
    A unique design feature of Trilinos is its focus on packages.
    """
    homepage = "https://trilinos.org/"
    url = "https://github.com/trilinos/Trilinos/archive/trilinos-release-12-6-4.tar.gz"

    version('12.6.4', 'c2ea7b5aa0d10bcabdb9b9a6e3bac3ea')
    version('12.6.1', '8aecea78546e7558f63ecc9a3b2949da')
    version('12.2.2', 'da4167310b32c4b2ebb0a8994138452b')

    def url_for_version(self, version):
        base_url = "https://github.com/trilinos/Trilinos/archive"
        parts = [str(p) for p in Version(version)]
        dash_ver = "-".join(parts)
        return "{0}/trilinos-release-{1}.tar.gz".format(base_url, dash_ver)
                            
    variant('metis',        default=True,  description='Compile with METIS and ParMETIS')
    variant('mumps',        default=False,  description='Compile with support for MUMPS solvers')
    variant('superlu-dist', default=False,  description='Compile with SuperluDist solvers')
    variant('hypre',        default=True,  description='Compile with Hypre preconditioner')
    variant('hdf5',         default=True,  description='Compile with HDF5')
    variant('suite-sparse', default=True,  description='Compile with SuiteSparse solvers')
    # not everyone has py-numpy activated, keep it disabled by default to avoid
    # configure errors
    variant('python',       default=False, description='Build python wrappers')
    variant('shared',       default=True,  description='Enables the build of shared libraries')
    variant('debug',        default=False, description='Builds a debug version of the libraries')
    variant('boost',        default=True, description='Compile with Boost')

    depends_on('cmake', type='build')

    # Everything should be compiled with -fpic
    depends_on('blas')
    depends_on('lapack')
    depends_on('boost', when='+boost')
    depends_on('matio')
    depends_on('glm')
    depends_on('swig')
    depends_on('metis@5:', when='+metis')
    depends_on('suite-sparse', when='+suite-sparse')

    # MPI related dependencies
    depends_on('mpi')
    depends_on('netcdf+mpi')
    depends_on('parmetis', when='+metis')
    # Trilinos' Tribits config system is limited which makes it very tricky to
    # link Amesos with static MUMPS, see
    # https://trilinos.org/docs/dev/packages/amesos2/doc/html/classAmesos2_1_1MUMPS.html
    # One could work it out by getting linking flags from mpif90 --showme:link
    # (or alike) and adding results to -DTrilinos_EXTRA_LINK_FLAGS together
    # with Blas and Lapack and ScaLAPACK and Blacs and -lgfortran and it may
    # work at the end. But let's avoid all this by simply using shared libs
    depends_on('mumps@5.0:+mpi+shared', when='+mumps')
    depends_on('scalapack', when='+mumps')
    depends_on('superlu-dist@:4.3', when='@:12.6.1+superlu-dist')
    depends_on('superlu-dist', when='@12.6.2:+superlu-dist')
    depends_on('hypre', when='+hypre')
    depends_on('hdf5+mpi', when='+hdf5')
    depends_on('python', when='+python')
    depends_on('py-numpy', when='+python')

    patch('umfpack_from_suitesparse.patch')

    # check that the combination of variants makes sense
    def variants_check(self):
        if '+superlu-dist' in self.spec and self.spec.satisfies('@:11.4.3'):
            # For Trilinos v11 we need to force SuperLUDist=OFF, since only the
            # deprecated SuperLUDist v3.3 together with an Amesos patch is
            # working.
            raise RuntimeError('The superlu-dist variant can only be used' +
                               ' with Trilinos @12.0.1:')

    def install(self, spec, prefix):
        self.variants_check()

        cxx_flags = []
        options = []
        options.extend(std_cmake_args)

        mpi_bin = spec['mpi'].prefix.bin
        # Note: -DXYZ_LIBRARY_NAMES= needs semicolon separated list of names
        options.extend([
            '-DTrilinos_ENABLE_ALL_PACKAGES:BOOL=ON',
            '-DTrilinos_ENABLE_ALL_OPTIONAL_PACKAGES:BOOL=ON',
            '-DTrilinos_VERBOSE_CONFIGURE:BOOL=OFF',
            '-DTrilinos_ENABLE_TESTS:BOOL=OFF',
            '-DTrilinos_ENABLE_EXAMPLES:BOOL=OFF',
            '-DCMAKE_BUILD_TYPE:STRING=%s' % (
                'DEBUG' if '+debug' in spec else 'RELEASE'),
            '-DBUILD_SHARED_LIBS:BOOL=%s' % (
                'ON' if '+shared' in spec else 'OFF'),
            '-DTPL_ENABLE_MPI:BOOL=ON',
            '-DMPI_BASE_DIR:PATH=%s' % spec['mpi'].prefix,
            '-DTPL_ENABLE_BLAS=ON',
            '-DBLAS_LIBRARY_NAMES=%s' % to_lib_name(
                spec['blas'].blas_shared_lib),
            '-DBLAS_LIBRARY_DIRS=%s' % spec['blas'].prefix.lib,
            '-DTPL_ENABLE_LAPACK=ON',
            '-DLAPACK_LIBRARY_NAMES=%s' % to_lib_name(
                spec['lapack'].lapack_shared_lib),
            '-DLAPACK_LIBRARY_DIRS=%s' % spec['lapack'].prefix.lib,
            '-DTrilinos_ENABLE_EXPLICIT_INSTANTIATION:BOOL=ON',
            '-DTrilinos_ENABLE_CXX11:BOOL=ON',
            '-DTPL_ENABLE_Netcdf:BOOL=ON',
            '-DTPL_ENABLE_HYPRE:BOOL=%s' % (
                'ON' if '+hypre' in spec else 'OFF')
        ])

        if '+hdf5' in spec:
            options.extend([
                '-DTPL_ENABLE_HDF5:BOOL=ON',
                '-DHDF5_INCLUDE_DIRS:PATH=%s' % spec['hdf5'].prefix.include,
                '-DHDF5_LIBRARY_DIRS:PATH=%s' % spec['hdf5'].prefix.lib
            ])
        else:
            options.extend(['-DTPL_ENABLE_HDF5:BOOL=OFF'])

        if '+boost' in spec:
            options.extend([
                '-DTPL_ENABLE_Boost:BOOL=ON',
                '-DBoost_INCLUDE_DIRS:PATH=%s' % spec['boost'].prefix.include,
                '-DBoost_LIBRARY_DIRS:PATH=%s' % spec['boost'].prefix.lib
            ])
        else:
            options.extend(['-DTPL_ENABLE_Boost:BOOL=OFF'])

        # Fortran lib
        libgfortran = os.path.dirname(os.popen(
            '%s --print-file-name libgfortran.a' %
            join_path(mpi_bin, 'mpif90')).read())
        options.extend([
            '-DTrilinos_EXTRA_LINK_FLAGS:STRING=-L%s/ -lgfortran' % (
                libgfortran),
            '-DTrilinos_ENABLE_Fortran=ON'
        ])

        # for build-debug only:
        # options.extend([
        #    '-DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE'
        # ])

        # suite-sparse related
        if '+suite-sparse' in spec:
            options.extend([
                # FIXME: Trilinos seems to be looking for static libs only,
                # patch CMake TPL file?
                '-DTPL_ENABLE_Cholmod:BOOL=OFF',
                # '-DTPL_ENABLE_Cholmod:BOOL=ON',
                # '-DCholmod_LIBRARY_DIRS:PATH=%s' % (
                #    spec['suite-sparse'].prefix.lib,
                # '-DCholmod_INCLUDE_DIRS:PATH=%s' % (
                #    spec['suite-sparse'].prefix.include,
                '-DTPL_ENABLE_UMFPACK:BOOL=ON',
                '-DUMFPACK_LIBRARY_DIRS:PATH=%s' % (
                    spec['suite-sparse'].prefix.lib),
                '-DUMFPACK_INCLUDE_DIRS:PATH=%s' % (
                    spec['suite-sparse'].prefix.include),
                '-DUMFPACK_LIBRARY_NAMES=umfpack;amd;colamd;cholmod;' +
                'suitesparseconfig'
            ])
        else:
            options.extend([
                '-DTPL_ENABLE_Cholmod:BOOL=OFF',
                '-DTPL_ENABLE_UMFPACK:BOOL=OFF',
            ])

        # metis / parmetis
        if '+metis' in spec:
            options.extend([
                '-DTPL_ENABLE_METIS:BOOL=ON',
                '-DMETIS_LIBRARY_DIRS=%s' % spec['metis'].prefix.lib,
                '-DMETIS_LIBRARY_NAMES=metis',
                '-DTPL_METIS_INCLUDE_DIRS=%s' % spec['metis'].prefix.include,
                '-DTPL_ENABLE_ParMETIS:BOOL=ON',
                '-DParMETIS_LIBRARY_DIRS=%s;%s' % (
                    spec['parmetis'].prefix.lib, spec['metis'].prefix.lib),
                '-DParMETIS_LIBRARY_NAMES=parmetis;metis',
                '-DTPL_ParMETIS_INCLUDE_DIRS=%s' % (
                    spec['parmetis'].prefix.include)
            ])
        else:
            options.extend([
                '-DTPL_ENABLE_METIS:BOOL=OFF',
                '-DTPL_ENABLE_ParMETIS:BOOL=OFF',
            ])

        # mumps / scalapack
        if '+mumps' in spec:
            options.extend([
                '-DTPL_ENABLE_MUMPS:BOOL=ON',
                '-DMUMPS_LIBRARY_DIRS=%s' % spec['mumps'].prefix.lib,
                # order is important!
                '-DMUMPS_LIBRARY_NAMES=dmumps;mumps_common;pord',
                '-DTPL_ENABLE_SCALAPACK:BOOL=ON',
                # FIXME: for MKL it's mkl_scalapack_lp64;mkl_blacs_mpich_lp64
                '-DSCALAPACK_LIBRARY_NAMES=scalapack'
            ])
            # see
            # https://github.com/trilinos/Trilinos/blob/master/packages/amesos/README-MUMPS
            cxx_flags.extend([
                '-DMUMPS_5_0'
            ])
        else:
            options.extend([
                '-DTPL_ENABLE_MUMPS:BOOL=OFF',
                '-DTPL_ENABLE_SCALAPACK:BOOL=OFF',
            ])

        # superlu-dist:
        if '+superlu-dist' in spec:
            # Amesos, conflicting types of double and complex SLU_D
            # see
            # https://trilinos.org/pipermail/trilinos-users/2015-March/004731.html
            # and
            # https://trilinos.org/pipermail/trilinos-users/2015-March/004802.html
            options.extend([
                '-DTeuchos_ENABLE_COMPLEX:BOOL=OFF',
                '-DKokkosTSQR_ENABLE_Complex:BOOL=OFF'
            ])
            options.extend([
                '-DTPL_ENABLE_SuperLUDist:BOOL=ON',
                '-DSuperLUDist_LIBRARY_DIRS=%s' %
                spec['superlu-dist'].prefix.lib,
                '-DSuperLUDist_INCLUDE_DIRS=%s' %
                spec['superlu-dist'].prefix.include
            ])
            if spec.satisfies('^superlu-dist@4.0:'):
                options.extend([
                    '-DHAVE_SUPERLUDIST_LUSTRUCTINIT_2ARG:BOOL=ON'
                ])
        else:
            options.extend([
                '-DTPL_ENABLE_SuperLUDist:BOOL=OFF',
            ])

        # python
        if '+python' in spec:
            options.extend([
                '-DPYTHON_EXECUTABLE:FILEPATH=%s/python' % spec['python'].prefix.bin,
                '-DTrilinos_ENABLE_PyTrilinos:BOOL=ON'
             ])
        else:
            options.extend([
                '-DTrilinos_ENABLE_PyTrilinos:BOOL=OFF'
            ])

        # collect CXX flags:
        options.extend([
            '-DCMAKE_CXX_FLAGS:STRING=%s' % (' '.join(cxx_flags)),
        ])

        # disable due to compiler / config errors:
        options.extend([
            '-DTrilinos_ENABLE_SEACAS=OFF',
            '-DTrilinos_ENABLE_Pike=OFF',
            '-DTrilinos_ENABLE_STK=OFF',
            '-DTrilinos_ENABLE_FEI=OFF'
        ])
        if sys.platform == 'darwin':
            options.extend([
                '-DTrilinos_ENABLE_FEI=OFF'
            ])

        with working_dir('spack-build', create=True):
            cmake('..', *options)
            make()
            make('install')

            # When trilinos is built with Python, libpytrilinos is included
            # through cmake configure files. Namely, Trilinos_LIBRARIES in
            # TrilinosConfig.cmake contains pytrilinos. This leads to a
            # run-time error: Symbol not found: _PyBool_Type and prevents
            # Trilinos to be used in any C++ code, which links executable
            # against the libraries listed in Trilinos_LIBRARIES.  See
            # https://github.com/Homebrew/homebrew-science/issues/2148#issuecomment-103614509
            # A workaround it to remove PyTrilinos from the COMPONENTS_LIST :
            if '+python' in self.spec:
                filter_file(r'(SET\(COMPONENTS_LIST.*)(PyTrilinos;)(.*)',
                            (r'\1\3'),
                            '%s/cmake/Trilinos/TrilinosConfig.cmake' %
                            prefix.lib)

            # The shared libraries are not installed correctly on Darwin;
            # correct this
            if (sys.platform == 'darwin') and ('+shared' in spec):
                fix_darwin_install_name(prefix.lib)
