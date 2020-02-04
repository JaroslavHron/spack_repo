# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
import sys
from spack import *


class Petsc(Package):
    """PETSc is a suite of data structures and routines for the scalable
    (parallel) solution of scientific applications modeled by partial
    differential equations.
    """

    homepage = "http://www.mcs.anl.gov/petsc/index.html"
    url      = "http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.5.3.tar.gz"
    git      = "https://github.com/firedrakeproject/petsc"

    maintainers = ['balay', 'barrysmith', 'jedbrown']

    version('develop', branch='master')
    version('xsdk-0.2.0', tag='xsdk-0.2.0')
    version('master-firedrake', branch='firedrake')

    #version('trunk-firedrake.2019.12.31', commit='49720042e5cd5f24a0fea16ff2f129ba53b17b9e', get_full_repo=True)
    #version('trunk-firedrake.2019.10.18', commit='edd0a2d9fa6ef4d7e0b754c00c43eb7e21ac31c6', get_full_repo=True)

    variant('shared',  default=True,
            description='Enables the build of shared libraries')
    variant('mpi',     default=True,  description='Activates MPI support')
    variant('double',  default=True,
            description='Switches between single and double precision')
    variant('complex', default=False, description='Build with complex numbers')
    variant('debug',   default=False, description='Compile in debug mode')

    variant('int64', default=False,
            description='Compile with 64bit indices')
    variant('clanguage', default='C', values=('C', 'C++'),
            description='Specify C (recommended) or C++ to compile PETSc',
            multi=False)
    variant('fftw', default=False,
            description='Activates support for FFTW (only parallel)')
    variant('suite-sparse', default=False,
            description='Activates support for SuiteSparse')
    variant(
            'firedrake', default=True,
            description='Additional external packages downloaded by petsc during build required by firedrake')

    
    variant('X', default=False,
            description='Activate X support')
    variant('batch', default=False,
            description='Enable when mpiexec is not available to run binaries')

    # 3.8.0 has a build issue with MKL - so list this conflict explicitly
    conflicts('^intel-mkl', when='@3.8.0')

    filter_compiler_wrappers(
        'petscvariables', relative_root='lib/petsc/conf'
    )

    # temporary workaround Clang 8.1.0 with XCode 8.3 on macOS, see
    # https://bitbucket.org/petsc/petsc/commits/4f290403fdd060d09d5cb07345cbfd52670e3cbc
    # the patch is an adaptation of the original commit to 3.7.5
    if sys.platform == "darwin":
        patch('macos-clang-8.1.0.diff',
              when='@3.7.5%clang@8.1.0:')
    patch('pkg-config-3.7.6-3.8.4.diff', when='@3.7.6:3.8.4')

    patch('xcode_stub_out_of_sync.patch', when='@:3.10.4')

    patch('xlf_fix-dup-petscfecreate.patch', when='@3.11.0')

    # Virtual dependencies
    # Git repository needs sowing to build Fortran interface
    depends_on('sowing', when='@develop')
    depends_on('sowing', when='@firedrake.2019:')
    depends_on('sowing', when='@master-firedrake')
    depends_on('sowing@1.1.23-p1', when='@xsdk-0.2.0')

    # PETSc, hypre, superlu_dist when built with int64 use 32 bit integers
    # with BLAS/LAPACK
    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi', when='+mpi')

    # Build dependencies
    depends_on('python@2.6:2.8', type='build', when='@:3.10.99')
    depends_on('python@2.6:2.8,3.4:', type='build', when='@3.11:')

    depends_on('fftw+mpi', when='+fftw+mpi')
    depends_on('suite-sparse', when='+suite-sparse')
    depends_on('libx11', when='+X')

    def mpi_dependent_options(self):
        if '~mpi' in self.spec:
            compiler_opts = [
                '--with-cc=%s' % os.environ['CC'],
                '--with-cxx=%s' % (os.environ['CXX']
                                   if self.compiler.cxx is not None else '0'),
                '--with-fc=%s' % (os.environ['FC']
                                  if self.compiler.fc is not None else '0'),
                '--with-mpi=0'
            ]
            error_message_fmt = \
                '\t{library} support requires "+mpi" to be activated'

            # If mpi is disabled (~mpi), it's an error to have any of these
            # enabled. This generates a list of any such errors.
            errors = [
                error_message_fmt.format(library=x)
                for x in ('hdf5', 'hypre', 'parmetis', 'mumps', 'superlu-dist')
                if ('+' + x) in self.spec]
            if errors:
                errors = ['incompatible variants given'] + errors
                raise RuntimeError('\n'.join(errors))
        else:
            compiler_opts = [
                '--with-cc=%s' % self.spec['mpi'].mpicc,
                '--with-cxx=%s' % self.spec['mpi'].mpicxx,
                '--with-fc=%s' % self.spec['mpi'].mpifc,
            ]
            if self.spec.satisfies('%intel'):
                # mpiifort needs some help to automatically link
                # all necessary run-time libraries
                compiler_opts.append('--FC_LINKER_FLAGS=-lintlc')
        return compiler_opts

    def install(self, spec, prefix):
        options = ['--with-ssl=0',
                   '--download-c2html=0',
                   '--download-sowing=0',
                   '--download-hwloc=0',
                   'CFLAGS=%s' % ' '.join(spec.compiler_flags['cflags']),
                   'FFLAGS=%s' % ' '.join(spec.compiler_flags['fflags']),
                   'CXXFLAGS=%s' % ' '.join(spec.compiler_flags['cxxflags'])]
        options.extend(self.mpi_dependent_options())
        options.extend([
            '--with-precision=%s' % (
                'double' if '+double' in spec else 'single'),
            '--with-scalar-type=%s' % (
                'complex' if '+complex' in spec else 'real'),
            '--with-shared-libraries=%s' % ('1' if '+shared' in spec else '0'),
            '--with-debugging=%s' % ('1' if '+debug' in spec else '0'),
            '--with-64-bit-indices=%s' % ('1' if '+int64' in spec else '0')
        ])
        if '+debug' not in spec:
            options.extend(['COPTFLAGS=',
                            'FOPTFLAGS=',
                            'CXXOPTFLAGS='])

        # Make sure we use exactly the same Blas/Lapack libraries
        # across the DAG. To that end list them explicitly
        lapack_blas = spec['lapack'].libs + spec['blas'].libs
        options.extend([
            '--with-blas-lapack-lib=%s' % lapack_blas.joined()
        ])

        if '+X' in spec:
            options.append('--with-x=1')
        else:
            options.append('--with-x=0')

        options.append('--with-cxx-dialect=C++11')

        # zlib: configuring using '--with-zlib-dir=...' has some issues with
        # SuiteSparse so specify directly the include path and the libraries.
        if 'zlib' in spec:
            options.extend([
                '--with-zlib-include=%s' % spec['zlib'].prefix.include,
                '--with-zlib-lib=%s'     % spec['zlib'].libs.joined(),
                '--with-zlib=1'
            ])
        else:
            options.append('--with-zlib=0')

        #firedrake-install --show-petsc-configure-options
        #--download-chaco --download-hdf5 --with-cxx-dialect=C++11 --download-hypre --download-mumps --download-netcdf --download-ml --download-mpich --download-ptscotch --with-shared-libraries=1 --download-metis --download-exodusii --download-pragmatic --download-pnetcdf --download-suitesparse --download-pastix --with-c2html=0 --with-fortran-bindings=0 --download-superlu_dist --with-debugging=0 --download-eigen=/home/hron/pkg/DEV/firedrake/firedrake/src/eigen-3.3.3.tgz --with-zlib --download-scalapack                              
        firedrake_pkgs=['chaco', 'hdf5', 'hypre', 'mumps', 'netcdf', 'ml', 'ptscotch', 'metis', 'exodusii', 'pragmatic', 'pnetcdf', 'suitesparse', 'pastix', 'superlu_dist', 'scalapack', 'triangle', 'ctetgen']
        for pkg in firedrake_pkgs:
            options.append('--download-%s' % pkg)
            
        options.append('--download-eigen={}'.format('https://github.com/eigenteam/eigen-git-mirror/archive/3.3.3.tar.gz'))
        options.append('--with-fortran-bindings=0')

        python('configure', '--prefix=%s' % prefix, *options)

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
                # For Spectrum MPI, if -np is omitted, the default behavior is
                # to assign one process per process slot, where the default
                # process slot allocation is one per core. On systems with
                # many cores, the number of processes can exceed the size of
                # the grid specified when the testcase is run and the test case
                # fails. Specify a small number of processes to prevent
                # failure.
                # For more information about Spectrum MPI invocation, see URL
                # https://www.ibm.com/support/knowledgecenter/en/SSZTET_10.1.0/smpi02/smpi02_mpirun_options.html
                if ('spectrum-mpi' in spec):
                    run.add_default_arg('-np')
                    run.add_default_arg('4')
                run('ex50', '-da_grid_x', '4', '-da_grid_y', '4')
                if 'superlu-dist' in spec:
                    run('ex50',
                        '-da_grid_x', '4',
                        '-da_grid_y', '4',
                        '-pc_type', 'lu',
                        '-pc_factor_mat_solver_package', 'superlu_dist')

                if 'mumps' in spec:
                    run('ex50',
                        '-da_grid_x', '4',
                        '-da_grid_y', '4',
                        '-pc_type', 'lu',
                        '-pc_factor_mat_solver_package', 'mumps')

                if 'hypre' in spec:
                    run('ex50',
                        '-da_grid_x', '4',
                        '-da_grid_y', '4',
                        '-pc_type', 'hypre',
                        '-pc_hypre_type', 'boomeramg')

    def setup_build_environment(self, env):
        # configure fails if these env vars are set outside of Spack
        env.unset('PETSC_DIR')
        env.unset('PETSC_ARCH')

    def setup_run_environment(self, env):
        # Set PETSC_DIR in the module file
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')

    def setup_dependent_build_environment(self, env, dependent_spec):
        # Set up PETSC_DIR for everyone using PETSc package
        env.set('PETSC_DIR', self.prefix)
        env.unset('PETSC_ARCH')

    @property
    def headers(self):
        return find_headers('petsc', self.prefix.include, recursive=False) \
            or None  # return None to indicate failure

    # For the 'libs' property - use the default handler.
