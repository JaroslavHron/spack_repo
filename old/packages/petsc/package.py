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
import os
from spack import *


class Petsc(Package):
    """
    PETSc is a suite of data structures and routines for the scalable
    (parallel) solution of scientific applications modeled by partial
    differential equations.
    """

    homepage = "http://www.mcs.anl.gov/petsc/index.html"
    url = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.5.3.tar.gz"

    version('3.7.2', '50da49867ce7a49e7a0c1b37f4ec7b34')
    version('3.6.4', '7632da2375a3df35b8891c9526dbdde7')

    variant('shared',  default=True,  description='Enables the build of shared libraries')
    variant('mpi',     default=True,  description='Activates MPI support')
    variant('double',  default=True,  description='Switches between single and double precision')
    variant('complex', default=False, description='Build with complex numbers')
    variant('debug',   default=False, description='Compile in debug mode')

    download_libs=['superlu', 'superlu_dist', 'hypre', 'scalapack', 'blacs', 'mumps', 'ml', 'suitesparse', 'pord', 'scotch', 'ptscotch']

    for lib in download_libs:
        variant(lib, default=True, description="Compile with internal {0} library".format(lib))

    variant('metis',   default=True,  description='Activates support for metis and parmetis')
    variant('hdf5',    default=True,  description='Activates support for HDF5 (only parallel)')
    variant('boost',   default=True,  description='Activates support for Boost')

    # Virtual dependencies
    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi', when='+mpi')

    # Build dependencies
    depends_on('python@2.6:2.7')

    # Other dependencies
    depends_on('boost', when='+boost')
    depends_on('flex', when='+ptscotch')
    depends_on('hdf5', when='+hdf5')
    depends_on('metis@5:', when='+metis')
    depends_on('parmetis', when='+metis+mpi')
            
    def mpi_dependent_options(self):
        if '~mpi' in self.spec:
            compiler_opts = [
                '--with-cc=%s' % os.environ['CC'],
                '--with-cxx=%s' % (os.environ['CXX'] if self.compiler.cxx is not None else '0'),  # NOQA: ignore=E501
                '--with-fc=%s' % (os.environ['FC'] if self.compiler.fc is not None else '0'),  # NOQA: ignore=E501
                '--with-mpi=0'
            ]
            error_message_fmt = '\t{library} support requires "+mpi" to be activated'  # NOQA: ignore=E501

            # If mpi is disabled (~mpi), it's an error to have any of these
            # enabled. This generates a list of any such errors.
            errors = [error_message_fmt.format(library=x)
                      for x in ('hdf5', 'hypre', 'parmetis', 'mumps', 'superlu-dist')  # NOQA: ignore=E501
                      if ('+' + x) in self.spec]
            if errors:
                errors = ['incompatible variants given'] + errors
                raise RuntimeError('\n'.join(errors))
        else:
            opt_flags='-O2 -mfpmath=sse -fexpensive-optimizations'
            compiler_opts = [
                '--with-mpi=1',
                '--with-mpi-dir=%s' % self.spec['mpi'].prefix,
                '--CFLAGS=-march=native -pipe',
                '--CXXFLAGS=-march=native -pipe',
                '--FFLAGS=-march=native -pipe',
                '--COPTFLAGS=%s' % opt_flags,
                '--CXXOPTFLAGS=%s' % opt_flags,
                '--FOPTFLAGS=%s' % opt_flags
            ]
        return compiler_opts

    def install(self, spec, prefix):
        options = ['--with-ssl=0','--with-x=0','--with-pic=1','--with-single-library=1','--with-clanguage=c','--with-c++-support']
        options.extend(self.mpi_dependent_options())
        options.extend([
            '--with-precision=%s' % ('double' if '+double' in spec else 'single'),  # NOQA: ignore=E501
            '--with-scalar-type=%s' % ('complex' if '+complex' in spec else 'real'),  # NOQA: ignore=E501
            '--with-shared-libraries=%s' % ('1' if '+shared' in spec else '0'),
            '--with-debugging=%s' % ('1' if '+debug' in spec else '0'),
            '--with-blas-lapack-dir=%s' % spec['lapack'].prefix
        ])
        
        # Activates library support if needed
        for library in ('boost', 'hdf5', 'metis', 'parmetis'):
            options.append(
                '--with-{library}={value}'.format(library=library, value=('1' if library in spec else '0'))  # NOQA: ignore=E501
            )
            if library in spec:
                options.append(
                    '--with-{library}-dir={path}'.format(library=library, path=spec[library].prefix)  # NOQA: ignore=E501
                )

        for lib in self.download_libs:
            if "+{0}".format(lib) in spec:
                options.append('--download-{library}=yes'.format(library=lib))
                                            
        configure('--prefix=%s' % prefix, *options)

        # PETSc has its own way of doing parallel make.
        make('MAKE_NP=%s' % make_jobs, parallel=False)
        make("install")

        # solve Poisson equation in 2D to make sure nothing is broken:
        if ('mpi' in spec) and self.run_tests:
            with working_dir('src/ksp/ksp/examples/tutorials'):
                env['PETSC_DIR'] = self.prefix
                cc = Executable(spec['mpi'].mpicc)
                cc('ex50.c', '-I%s' % prefix.include, '-L%s' % prefix.lib,
                   '-lpetsc', '-lm', '-o', 'ex50')
                run = Executable(join_path(spec['mpi'].prefix.bin, 'mpirun'))
                run('ex50', '-da_grid_x', '4', '-da_grid_y', '4')
                if 'superlu-dist' in spec:
                    run('ex50', '-da_grid_x', '4', '-da_grid_y', '4', '-pc_type', 'lu', '-pc_factor_mat_solver_package', 'superlu_dist')  # NOQA: ignore=E501

                if 'mumps' in spec:
                    run('ex50', '-da_grid_x', '4', '-da_grid_y', '4', '-pc_type', 'lu', '-pc_factor_mat_solver_package', 'mumps')  # NOQA: ignore=E501

                if 'hypre' in spec:
                    run('ex50', '-da_grid_x', '4', '-da_grid_y', '4', '-pc_type', 'hypre', '-pc_hypre_type', 'boomeramg')  # NOQA: ignore=E501

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        # set up PETSC_DIR for everyone using PETSc package
        spack_env.set('PETSC_DIR', self.prefix)
