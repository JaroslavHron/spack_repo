import os
import sys
from spack import *

class Firedrake(PythonPackage):
    """
    """

    homepage = "https://www.firedrakeproject.org"
    url      = "https://github.com/firedrakeproject/firedrake"
    git      = 'https://github.com/firedrakeproject/firedrake'
    
    version('2019.05.29', tag='Firedrake_20190529.1')
    #version('master', branch='master')

    depends_on('firedrake.fiat')
    depends_on('firedrake.finat')
    depends_on('firedrake.ufl')
    depends_on('firedrake.tsfc')
    depends_on('firedrake.pyop2')

    depends_on('boost')
    depends_on('libspatialindex')
    depends_on('libsupermesh')

    # This are the build dependencies
    depends_on('py-setuptools')
    depends_on('cmake')
    depends_on('pkgconfig')
    depends_on('mpi')

    depends_on('py-ply')
    depends_on('py-six')
    depends_on('py-cython')
    depends_on('py-cachetools')
    
    depends_on('py-numpy')
    depends_on('py-sympy')
    depends_on('py-scipy')
    depends_on('py-randomgen')

    depends_on('py-mpi4py')

    #depends_on('sundials@:3.2.1', when='+sundials')
    
    depends_on('petsc +eigen')
    depends_on('slepc')
    depends_on('py-petsc4py')
    depends_on('py-slepc4py')

    depends_on('py-matplotlib')
    depends_on('hdf5')
    depends_on('py-h5py')

    @run_before('build')
    def fixme(self):
        filter_file(r'"firedrake.matrix_free"','"firedrake.matrix_free", "firedrake.slate", "firedrake.slate.slac", "firedrake.slate.static_condensation", "firedrake.preconditioners"', 'setup.py')
        
    @run_after('install')
    def post_install(self):
        config='{}/lib/python3.6/site-packages/firedrake_configuration/configuration.json'.format(self.prefix)
        with open(config, 'w') as conf_file:
            conf_file.write('{"options": {"honour_pythonpath": true, "honour_petsc_dir": true}}')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = [  ]
        return args

    def install_args(self, spec, prefix):
        args = ['--prefix={0}'.format(prefix)]
        return args

