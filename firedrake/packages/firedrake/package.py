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
    depends_on('firedrake.libspatialindex')
    depends_on('libsupermesh')

    # This are the build dependencies
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
    
    #firedrake-install --show-petsc-configure-options
    #--download-eigen=/home/hron/firedrake/firedrake/src/eigen-3.3.3.tgz --with-fortran-bindings=0 --download-chaco --download-metis --download-parmetis --download-scalapack --download-hypre --download-mumps --with-zlib --download-netcdf --download-hdf5 --download-pnetcdf --download-exodusii

    depends_on('firedrake.petsc@firedrake-2019.05.29 +firedrake ~trilinos ~hypre')
    depends_on('firedrake.slepc@firedrake-2019.05.29')
    #depends_on('firedrake.petsc@firedrake +firedrake ~trilinos ~hypre')
    #depends_on('firedrake.slepc@firedrake')
    #depends_on('petsc +firedrake ~trilinos ~hypre')

    depends_on('firedrake.py-petsc4py@firedrake-2019.05.29')
    depends_on('firedrake.py-slepc4py@firedrake-2019.05.29')
    #depends_on('firedrake.py-petsc4py@firedrake')
    #depends_on('firedrake.py-slepc4py@firedrake')

    depends_on('py-matplotlib')
    depends_on('hdf5')
    depends_on('py-h5py')

    phases = ['build_ext', 'install']

    patch('pf_use_coffee.patch')

    # fix subpackage instalations
    @run_before('build_ext')
    def fixme(self):
        filter_file(r'"firedrake.matrix_free"','"firedrake.matrix_free", "firedrake.slate", "firedrake.slate.slac", "firedrake.slate.static_condensation", "firedrake.preconditioners"', 'setup.py')

    # create configuration.json
    @run_after('install')
    def post_install(self):
        config='{}/lib/python3.6/site-packages/firedrake_configuration/configuration.json'.format(self.prefix)
        with open(config, 'w') as conf_file:
            conf_file.write('{"options": {"honour_pythonpath": true, "honour_petsc_dir": true}}')

    # add 2 lib dependeces - no idea why they are not found...
    def build_ext_args(self, spec, prefix):
        args = [ 
            '--library-dirs={0}/lib:{1}/lib'.format(spec['libspatialindex'].prefix,spec['libsupermesh'].prefix),
        ]
        return args
