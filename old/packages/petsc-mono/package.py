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
    git      = "https://bitbucket.org/petsc/petsc.git"

    maintainers = ['balay', 'barrysmith', 'jedbrown']

    version('develop', branch='master')
    version('xsdk-0.2.0', tag='xsdk-0.2.0')

    version('3.10.3', 'cd106babbae091604fee40c258737c84dec048949be779eaef5a745df3dc8de4')
    version('3.10.2', '63ed950653ae9b8d19daea47e24c0338')
    version('3.10.1', '2d0d5a9bd8112a4147a2a23f7f62a906')
    version('3.10.0', '0240c2ce8c54e47b3531a743ee844d41')
    version('3.9.4', 'c98eb67573efb2f91c6f239368259e44')
    version('3.9.3', '7b71d705f66f9961cb0e2da3f9da79a1')
    version('3.9.2', '8bedc0cd8c8603d54bfd99a6e8f77b3d')
    version('3.9.1', 'd3a229a188dbeef9b3f29b9a63622fad')
    version('3.9.0', '34b8a81814ca050a96d58e53a2f0ac7a')
    version('3.8.4', 'd7767fe2919536aa393eb22841899306')
    version('3.8.3', '322cbcf2a0f7b7bad562643b05d66f11')
    version('3.8.2', '00666e1c4cbfa8dd6eebf91ff8180f79')
    version('3.8.1', '3ed75c1147800fc156fe1f1e515a68a7')
    version('3.8.0', '02680f1f78a0d4c5a9de80a366793eb8')
    version('3.7.7', 'c2cfb76677d32839810c4cf51a2f9cf5')
    version('3.7.6', '977aa84b85aa3146c695592cd0a11057')
    version('3.7.5', 'f00f6e6a3bac39052350dd47194b58a3')
    version('3.7.4', 'aaf94fa54ef83022c14091f10866eedf')
    version('3.7.2', '50da49867ce7a49e7a0c1b37f4ec7b34')
    version('3.6.4', '7632da2375a3df35b8891c9526dbdde7')
    version('3.6.3', '91dd3522de5a5ef039ff8f50800db606')
    version('3.5.3', 'd4fd2734661e89f18ac6014b5dd1ef2f')
    version('3.5.2', 'ad170802b3b058b5deb9cd1f968e7e13')
    version('3.5.1', 'a557e029711ebf425544e117ffa44d8f')
    version('3.4.4', '7edbc68aa6d8d6a3295dd5f6c2f6979d')

    variant('download',  default=True,  description='Download all packages')
    variant('shared',  default=True,  description='Enables the build of shared libraries')
    variant('mpi',     default=True,  description='Activates MPI support')
    variant('double',  default=True,
            description='Switches between single and double precision')
    variant('complex', default=False, description='Build with complex numbers')
    variant('debug',   default=False, description='Compile in debug mode')
    variant('int64', default=False, description='Compile with 64bit indices')
    variant('clanguage', default='C', values=('C', 'C++'), description='Specify C (recommended) or C++ to compile PETSc', multi=False)

    download_libs=['superlu', 'superlu_dist', 'hypre', 'scalapack', 'blacs', 'mumps', 'ml', 'suitesparse', 'pord', 'scotch', 'ptscotch', 'triangle']

    for lib in download_libs:
        variant(lib, default=True, description="Compile with internal {0} library".format(lib))

    variant('metis',   default=True,  description='Activates support for metis and parmetis')
    variant('hdf5',    default=True,  description='Activates support for HDF5 (only parallel)')
    variant('boost',   default=True,  description='Activates support for Boost')

    # Virtual dependencies
    # Git repository needs sowing to build Fortran interface
    depends_on('sowing', when='@develop')

    # PETSc, hypre, superlu_dist when built with int64 use 32 bit integers
    # with BLAS/LAPACK
    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi', when='+mpi')

    # Build dependencies
    # wait for fix for build dependeces in spack
    #depends_on('python@2.6:2.8', type='build')
    #depends_on('python', type='build')

    # Other dependencies
    depends_on('boost', when='+boost')
    depends_on('flex', when='+ptscotch')
    depends_on('metis@5:~int64+real64', when='+metis~int64+double')
    depends_on('metis@5:+int64', when='+metis+int64~double')

    depends_on('hdf5+mpi+hl+fortran', when='+hdf5+mpi')
    depends_on('zlib', when='+hdf5')
    depends_on('parmetis', when='+metis+mpi')
            
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
                '--with-fc=%s' % self.spec['mpi'].mpifc
            ]
        return compiler_opts

    def install(self, spec, prefix):
        options = ['--with-ssl=0',
                   '--with-pic=1',
                   '--with-single-library=1',
                   '--with-clanguage=c',
                   '--with-c++-support'
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

        if 'trilinos' in spec:
            options.append('--with-cxx-dialect=C++11')

        if self.spec.satisfies('clanguage=C++'):
            options.append('--with-clanguage=C++')
        else:
            options.append('--with-clanguage=C')

        # Help PETSc pick up Scalapack from MKL:
        if 'scalapack' in spec:
            scalapack = spec['scalapack'].libs
            options.extend([
                '--with-scalapack-lib=%s' % scalapack.joined(),
                '--with-scalapack=1'
            ])
        else:
            options.extend([
                '--with-scalapack=0'
            ])

        # Activates library support if needed
        for library in ('boost', 'hdf5', 'metis', 'parmetis'):
            options.append(
                '--with-{library}={value}'.format(
                    library=library, value=('1' if library in spec else '0'))
            )
            if library in spec:
                options.append(
                    '--with-{library}-dir={path}'.format(
                        library=library, path=spec[library].prefix)
                )

        for lib in self.download_libs:
            if "+{0}".format(lib) in spec:
                options.append('--download-{library}=yes'.format(library=lib))
                                            
        #configure('--prefix=%s' % prefix, *options)
        Executable('/usr/bin/python')('./config/configure.py', '--prefix=%s' % prefix, *options)
        
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

    def setup_environment(self, spack_env, run_env):
        # configure fails if these env vars are set outside of Spack
        spack_env.unset('PETSC_DIR')
        spack_env.unset('PETSC_ARCH')

        spack_env.unset('PYTHONPATH')
        spack_env.unset('PYTHONHOME')
                
        # Set PETSC_DIR in the module file
        run_env.set('PETSC_DIR', self.prefix)
        run_env.unset('PETSC_ARCH')

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        # Set up PETSC_DIR for everyone using PETSc package
        spack_env.set('PETSC_DIR', self.prefix)
        spack_env.unset('PETSC_ARCH')

    @property
    def headers(self):
        return find_headers('petsc', self.prefix.include, recursive=False) \
            or None  # return None to indicate failure

    # For the 'libs' property - use the default handler.
