import os
import sys
from spack import *

class Mshr(CMakePackage):
    """mshr

    mshr is the mesh generation component of FEniCS. It generates
    simplicial DOLFIN meshes in 2D and 3D from geometries described by
    Constructive Solid Geometry (CSG) or from surface files, utilizing
    CGAL and Tetgen as mesh generation backends.
    """

    homepage = "https://bitbucket.org/fenics-project/mshr"
    url      = "https://bitbucket.org/fenics-project/mshr/downloads/mshr-2016.1.0.tar.gz"
    git='https://bitbucket.org/fenics-project/mshr'

    version('2018.1.0', tag='2018.1.0')
    version('2017.2.0', tag='2017.2.0')
    version('2017.1.0', tag='2017.1.0.post0')

    for ver in ['@2018.1.0','@2017.2.0','@2017.1.0'] :
        depends_on('dolfin{0}'.format(ver), type=("build","run"), when=ver)

    depends_on('boost')
    depends_on('gmp')
    depends_on('mpfr')
    depends_on('mpi')
    depends_on('eigen@3.2.0:')
    
    # This are the build dependencies
    depends_on('py-setuptools')
    depends_on('cmake')
    depends_on('swig')

    extends('python')
    
    def cmake_is_on(self, option):
        return 'ON' if option in self.spec else 'OFF'

    def cmake_args(self):
        spec = self.spec
        
        opts = [
            '-DCMAKE_BUILD_TYPE:STRING={0}'.format('Debug' if 'debug' in spec else 'Release'),
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DDOLFIN_SKIP_BUILD_TESTS:BOOL=OFF',
            '-DDOLFIN_AUTO_DETECT_MPI:BOOL=OFF',
            '-DCMAKE_USE_RELATIVE_PATHS:BOOL=ON',
            '-DDOLFIN_USE_PYTHON3={0}'.format('OFF' if spec['python'].version < Version('3.0.0') else 'ON'),
            '-DPYTHON_EXECUTABLE:FILEPATH={0}/python'.format(spec['python'].prefix.bin)
        ]

        os.environ['CC'] = spec['mpi'].mpicc
        os.environ['CXX'] = spec['mpi'].mpicxx
        os.environ['F77'] = spec['mpi'].mpif77
        os.environ['FC'] = spec['mpi'].mpifc

        os.environ['MPFR_DIR'] = spec['mpfr'].prefix
        
        return(opts)
