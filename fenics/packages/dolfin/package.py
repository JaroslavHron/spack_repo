import os
import sys
from spack import *

class Dolfin(CMakePackage):
    """DOLFIN

    DOLFIN is the computational backend of FEniCS and implements the
    FEniCS Problem Solving Environment in Python and C++.

    """

    homepage = "https://bitbucket.org/fenics-project/dolfin"
    url      = "https://bitbucket.org/fenics-project/dolfin/downloads/dolfin-2016.1.0.tar.gz"
    git      = 'https://bitbucket.org/fenics-project/dolfin'
    
    version('2018.1.0', tag='2018.1.0.post2')
    version('2017.2.0', tag='2017.2.0.post0')
    version('2017.1.0', tag='2017.1.0.post0')

    for ver in ['2018.1.0','2017.2.0','2017.1.0'] :
        wver='@'+ver
        depends_on('fiat{0}'.format(wver), type=("build","run"), when=wver)
        if( Version(ver) < Version('2018.1.0') ) :
            depends_on('instant{0}'.format(wver), type=("build","run"), when=wver)
        depends_on('dijitso{0}'.format(wver), type=("build","run"), when=wver)
        depends_on('ufl{0}'.format(wver), type=("build","run"), when=wver)
        depends_on('ffc{0}'.format(wver), type=("build","run"), when=wver)

    depends_on('boost')
    depends_on('eigen@3.2.0:')
    depends_on('libxml2')
    depends_on('pkgconfig')
    depends_on('mpi', when='+mpi')

    # back ports to python2 - not working in spack
    #depends_on('py-functools32', type=('build', 'run'), when='@2017.1.0:^python@:2.7')
    #depends_on('py-subprocess32', type=('build', 'run'), when='@2017.1.0:^python@:2.7')
    depends_on('py-ply')
    depends_on('py-six')
    depends_on('py-pybind11', when='@2018.1.0:')
    
    depends_on('py-numpy')
    depends_on('py-sympy')
    depends_on('py-scipy')

    depends_on('py-mpi4py', when='+mpi')

    depends_on('sundials@:3.2.1', when='+sundials')
    
    depends_on('petsc', when='+petsc')
    depends_on('slepc', when='+slepc')
    depends_on('py-petsc4py', when='+petsc4py')
    depends_on('py-slepc4py', when='+slepc4py')

    depends_on('py-matplotlib')
    depends_on('py-sphinx', when='+doc')

    depends_on('hdf5', when='+hdf5')

    depends_on('scotch', when='+scotch')
    depends_on('trilinos', when='+trilinos')

    depends_on('vtk', when='+vtk')

    depends_on('suite-sparse', when='+suitesparse')

    extends('python')
    
    # This are the build dependencies
    depends_on('py-setuptools')
    depends_on('cmake')
    depends_on('swig')

    variant('petsc',        default=True,  description='Compile with PETSc')
    variant('sundials',     default=True,  description='Compile with sundials')
    variant('hdf5',         default=True,  description='Compile with HDF5')
    variant('scotch',       default=True,  description='Compile with Scotch')
    variant('slepc',        default=True,  description='Compile with SLEPc')
    variant('trilinos',     default=True,  description='Compile with Trilinos')
    variant('suitesparse',  default=True,  description='Compile with SuiteSparse solvers')
    variant('vtk',          default=False, description='Compile with VTK')
    variant('mpi',          default=True,  description='Enables the distributed memory support')
    variant('shared',       default=True,  description='Enables the build of shared libraries')
    variant('debug',        default=False, description='Builds a debug version of the libraries')

    variant('mpi4py',     default=True,  description='Uses mpi4py')
    variant('petsc4py',     default=True,  description='Uses PETSc4py')
    variant('slepc4py',     default=True,  description='Uses SLEPc4py')

    variant('pastix',       default=False,  description='Compile with Pastix')

    variant('doc',     default=True,  description='Create docs.')
    
    def cmake_args(self):
        spec = self.spec
        
        opts = [
            '-DCMAKE_C_COMPILER={0}'.format(spec['mpi'].mpicc), 
            '-DCMAKE_CXX_COMPILER={0}'.format(spec['mpi'].mpicxx) ,
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DDOLFIN_SKIP_BUILD_TESTS:BOOL=OFF',
            '-DDOLFIN_ENABLE_DOCS:BOOL={0}'.format(self.cmake_is_on('doc')),
            '-DDOLFIN_AUTO_DETECT_MPI:BOOL=OFF',
            '-DDOLFIN_USE_PYTHON3={0}'.format('OFF' if spec['python'].version < Version('3.0.0') else 'ON'),
            '-DPYTHON_EXECUTABLE:FILEPATH={0}/python'.format(spec['python'].prefix.bin),
            '-DDOLFIN_ENABLE_OPENMP:BOOL=OFF',
            '-DDOLFIN_ENABLE_CHOLMOD:BOOL={0}'.format(self.cmake_is_on('suite-sparse')),
            '-DDOLFIN_ENABLE_MPI:BOOL={0}'.format(self.cmake_is_on('mpi')),
            '-DDOLFIN_ENABLE_PARMETIS:BOOL=OFF',
            '-DDOLFIN_ENABLE_PETSC:BOOL={0}'.format(self.cmake_is_on('petsc')),
            '-DPETSC_DIR:PATH={0}'.format(spec['petsc'].prefix),
            '-DDOLFIN_ENABLE_PETSC4PY:BOOL={0}'.format(self.cmake_is_on('py-petsc4py')),
            '-DDOLFIN_ENABLE_PYTHON:BOOL={0}'.format(self.cmake_is_on('python')),
            '-DDOLFIN_ENABLE_SCOTCH:BOOL={0}'.format(self.cmake_is_on('scotch')),
            '-DDOLFIN_ENABLE_SLEPC:BOOL={0}'.format(self.cmake_is_on('slepc')),
            '-DSLEPC_DIR:PATH={0}'.format(spec['slepc'].prefix),
            '-DDOLFIN_ENABLE_SLEPC4PY:BOOL={0}'.format(self.cmake_is_on('py-slepc4py')),
            '-DDOLFIN_ENABLE_SPHINX:BOOL={0}'.format(self.cmake_is_on('py-sphinx')),
            '-DDOLFIN_ENABLE_TRILINOS:BOOL={0}'.format(self.cmake_is_on('trilinos')),
            '-DDOLFIN_ENABLE_UMFPACK:BOOL={0}'.format(self.cmake_is_on('suite-sparse')),
            '-DDOLFIN_ENABLE_VTK:BOOL={0}'.format(self.cmake_is_on('vtk')),
            '-DDOLFIN_ENABLE_ZLIB:BOOL={0}'.format(self.cmake_is_on('zlib'))
        ]
        
        if '+sundials' in spec:
            opts.extend([
                '-DDOLFIN_ENABLE_SUNDIALS:BOOL={0}'.format(self.cmake_is_on('sundials')),
                '-DSUNDIALS_DIR:PATH={0}'.format(spec['sundials'].prefix)
            ])

        if '+hdf5' in spec:
            opts.extend([
                '-DDOLFIN_ENABLE_HDF5:BOOL=ON',
                '-DHDF5_DIR:PATH={0}'.format(spec['hdf5'].prefix),
                '-DHDF5_ROOT:PATH={0}'.format(spec['hdf5'].prefix),
                '-DHDF5_INCLUDE_DIRS={0}/include'.format(spec['hdf5'].prefix)
            ])

        if '+shared' in spec:
            opts.append('-DSHARED:BOOL=ON')

        os.environ['CC'] = spec['mpi'].mpicc
        os.environ['CXX'] = spec['mpi'].mpicxx
        os.environ['F77'] = spec['mpi'].mpif77
        os.environ['FC'] = spec['mpi'].mpifc
        
        os.environ['PETSC_DIR'] = spec['petsc'].prefix
        os.environ['SLEPC_DIR'] = spec['slepc'].prefix
        os.environ['MPFR_DIR'] = spec['mpfr'].prefix
        if 'py-sphinx' in self.spec : os.environ['SPHINX_DIR'] = spec['py-sphinx'].prefix
        os.environ['SCOTCH_DIR'] = spec['scotch'].prefix
        os.environ['HDF5_DIR'] = spec['hdf5'].prefix
        os.environ['HDF5_ROOT'] = spec['hdf5'].prefix
                                                                                           
        return opts
                
    def cmake_is_on(self, option):
        return 'ON' if option in self.spec else 'OFF'

