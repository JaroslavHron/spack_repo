import os
import sys
from spack import *

class Mshr(Package):
    """mshr

    mshr is the mesh generation component of FEniCS. It generates
    simplicial DOLFIN meshes in 2D and 3D from geometries described by
    Constructive Solid Geometry (CSG) or from surface files, utilizing
    CGAL and Tetgen as mesh generation backends.
    """

    homepage = "https://bitbucket.org/fenics-project/mshr"
    url      = "https://bitbucket.org/fenics-project/mshr/downloads/mshr-2016.1.0.tar.gz"

    version('2016.1.0', git='https://bitbucket.org/fenics-project/mshr', tag='mshr-2016.1.0')
    version('1.6.0', git='https://bitbucket.org/fenics-project/mshr', tag='mshr-1.6.0')
    version('1.7.0dev', git='https://bitbucket.org/fenics-project/mshr', commit='6e7cd5cd80e2d0c5c3040b19ac9f08b506be6727')

    for ver in ['@2016.1.0','@1.7.0dev','@1.6.0'] :
        depends_on('dolfin{0}'.format(ver), type=("build","run"), when=ver)

    extends('python')
    #depends_on('python@2.6:2.7')

    depends_on('boost')
    depends_on('gmp')
    depends_on('mpfr')
    depends_on('mpi')

    # This are the build dependencies
    depends_on('py-setuptools')
    depends_on('cmake@2.8.12:')
    depends_on('swig')

    def cmake_is_on(self, option):
        return 'ON' if option in self.spec else 'OFF'

    def install(self, spec, prefix):
        os.environ['CC'] = spec['mpi'].mpicc
        os.environ['CXX'] = spec['mpi'].mpicxx
        os.environ['F77'] = spec['mpi'].mpif77
        os.environ['FC'] = spec['mpi'].mpifc

        os.environ['MPFR_DIR'] = spec['mpfr'].prefix
        
        cmake_args = [
            '-DCMAKE_BUILD_TYPE:STRING={0}'.format('Debug' if 'debug' in spec else 'Release'),
            '-DBUILD_SHARED_LIBS:BOOL=ON',
            '-DCMAKE_PREFIX_PATH:PATH={0}'.format(prefix),
            '-DPYTHON_EXECUTABLE:FILEPATH={0}/python'.format(spec['python'].prefix.bin),
        ]
        cmake_args.extend(std_cmake_args)
        with working_dir('build', create=True):
            cmake('..', *cmake_args)
            make()
            make('install')
