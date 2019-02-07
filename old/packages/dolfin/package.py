import os
import sys
from spack import *

class Dolfin(Package):
    """DOLFIN

    DOLFIN is the computational backend of FEniCS and implements the
    FEniCS Problem Solving Environment in Python and C++.

    """

    homepage = "https://bitbucket.org/fenics-project/dolfin"
    url      = "https://bitbucket.org/fenics-project/dolfin/downloads/dolfin-2016.1.0.tar.gz"

    version('2016.1.0', git='https://bitbucket.org/fenics-project/dolfin', tag='dolfin-2016.1.0')
    version('1.6.0', git='https://bitbucket.org/fenics-project/dolfin', tag='dolfin-1.6.0')
    version('1.7.0dev', git='https://bitbucket.org/fenics-project/dolfin', branch='jan/fix-slow-real')

    for ver in ['@2016.1.0','@1.7.0dev','@1.6.0'] :
        depends_on('fiat{0}'.format(ver), type=("build","run"), when=ver)
        depends_on('instant{0}'.format(ver), type=("build","run"), when=ver)
        depends_on('ufl{0}'.format(ver), type=("build","run"), when=ver)
        depends_on('ffc{0}'.format(ver), type=("build","run"), when=ver)

    extends('python')
    #depends_on('python@2.6:2.7')

    depends_on('boost')
    depends_on('eigen@3.2.0:')
    depends_on('libxml2+python')
    depends_on('mpi', when='+mpi')

    depends_on('py-numpy')
    depends_on('py-ply')
    depends_on('py-six')
    depends_on('py-sympy')

    depends_on('py-mpi4py', when='+mpi')

    depends_on('petsc', when='+petsc')
    depends_on('slepc', when='+slepc')
    depends_on('py-petsc4py', when='+petsc4py')
    depends_on('py-slepc4py', when='+slepc4py')

    depends_on('petsc@:3.6.9', when='@:1.7.0+petsc')
    depends_on('slepc@:3.6.9', when='@:1.7.0+slepc')
    depends_on('py-petsc4py@:3.6.9', when='@:1.7+petsc4py')
    depends_on('py-slepc4py@:3.6.9', when='@:1.7+slepc4py')

    depends_on('py-matplotlib')
    depends_on('py-sphinx@1.0.1:', when='+doc')

    depends_on('hdf5@:1.9.0', when='@:1.8+hdf5')
    depends_on('hdf5', when='@2016.0.0:+hdf5')

    depends_on('scotch', when='+scotch')
    depends_on('trilinos', when='+trilinos')

    depends_on('vtk+opengl2+sw', when='@2016.0.0:+vtk')
    depends_on('vtk@5.10.1+opengl2+sw', when='@:1.8+vtk')

    depends_on('suite-sparse', when='+suitesparse')

    # This are the build dependencies
    depends_on('py-setuptools')
    depends_on('cmake@2.8.12:')
    depends_on('swig')

    variant('petsc',        default=True,  description='Compile with PETSc')
    variant('hdf5',         default=True,  description='Compile with HDF5')
    variant('scotch',       default=True,  description='Compile with Scotch')
    variant('slepc',        default=True,  description='Compile with SLEPc')
    variant('trilinos',     default=True,  description='Compile with Trilinos')
    variant('suitesparse',  default=True,  description='Compile with SuiteSparse solvers')
    variant('vtk',          default=True, description='Compile with VTK')
    variant('mpi',          default=True,  description='Enables the distributed memory support')
    variant('shared',       default=True,  description='Enables the build of shared libraries')
    variant('debug',        default=False, description='Builds a debug version of the libraries')

    variant('mpi4py',     default=True,  description='Uses mpi4py')
    variant('petsc4py',     default=True,  description='Uses PETSc4py')
    variant('slepc4py',     default=True,  description='Uses SLEPc4py')

    variant('pastix',       default=False,  description='Compile with Pastix')

    variant('doc',     default=True,  description='Create docs.')
    
    def cmake_is_on(self, option):
        return 'ON' if option in self.spec else 'OFF'

    def install(self, spec, prefix):
        os.environ['CC'] = spec['mpi'].mpicc
        os.environ['CXX'] = spec['mpi'].mpicxx
        os.environ['F77'] = spec['mpi'].mpif77
        os.environ['FC'] = spec['mpi'].mpifc

        os.environ['PETSC_DIR'] = spec['petsc'].prefix
        os.environ['MPFR_DIR'] = spec['mpfr'].prefix
        os.environ['SPHINX_DIR'] = spec['py-sphinx'].prefix
        os.environ['HDF5_DIR'] = spec['hdf5'].prefix
        os.environ['HDF5_ROOT'] = spec['hdf5'].prefix
        os.environ['FFC_DIR'] = spec['ffc'].prefix
        
        cmake_args = [
            '-DCMAKE_BUILD_TYPE:STRING={0}'.format('Debug' if 'debug' in spec else 'Release'),
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DDOLFIN_SKIP_BUILD_TESTS:BOOL=OFF',
            '-DDOLFIN_AUTO_DETECT_MPI:BOOL=OFF',
            '-DCMAKE_USE_RELATIVE_PATHS:BOOL=ON',
            '-DPYTHON_EXECUTABLE:FILEPATH={0}/python'.format(spec['python'].prefix.bin),
            '-DDOLFIN_ENABLE_OPENMP:BOOL=OFF',
            '-DDOLFIN_ENABLE_CHOLMOD:BOOL={0}'.format(self.cmake_is_on('suite-sparse')),
            '-DDOLFIN_ENABLE_MPI:BOOL={0}'.format(self.cmake_is_on('mpi')),
            '-DDOLFIN_ENABLE_PARMETIS:BOOL=OFF',
            '-DDOLFIN_ENABLE_PETSC:BOOL={0}'.format(self.cmake_is_on('petsc')),
            '-DDOLFIN_ENABLE_PETSC4PY:BOOL={0}'.format(self.cmake_is_on('py-petsc4py')),
            '-DDOLFIN_ENABLE_PYTHON:BOOL={0}'.format(self.cmake_is_on('python')),
            '-DDOLFIN_ENABLE_SCOTCH:BOOL={0}'.format(self.cmake_is_on('scotch')),
            '-DDOLFIN_ENABLE_SLEPC:BOOL={0}'.format(self.cmake_is_on('slepc')),
            '-DDOLFIN_ENABLE_SLEPC4PY:BOOL={0}'.format(self.cmake_is_on('py-slepc4py')),
            '-DDOLFIN_ENABLE_SPHINX:BOOL={0}'.format(self.cmake_is_on('py-sphinx')),
            '-DDOLFIN_ENABLE_TRILINOS:BOOL={0}'.format(self.cmake_is_on('trilinos')),
            '-DDOLFIN_ENABLE_UMFPACK:BOOL={0}'.format(self.cmake_is_on('suite-sparse')),
            '-DDOLFIN_ENABLE_VTK:BOOL={0}'.format(self.cmake_is_on('vtk')),
            '-DDOLFIN_ENABLE_ZLIB:BOOL={0}'.format(self.cmake_is_on('zlib'))
        ]

        if '+hdf5' in spec:
            cmake_args.extend([
                '-DDOLFIN_ENABLE_HDF5:BOOL=ON',
                '-DHDF5_DIR:PATH={0}'.format(spec['hdf5'].prefix),
                '-DHDF5_ROOT:PATH={0}'.format(spec['hdf5'].prefix),
                '-DHDF5_INCLUDE_DIRS={0}/include'.format(spec['hdf5'].prefix)
            ])
        
        cmake_args.extend(std_cmake_args)

        with working_dir('build', create=True):
            cmake('..', *cmake_args)
            make()
            make('install')
