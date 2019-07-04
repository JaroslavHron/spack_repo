from spack import *

class Pyop2(PythonPackage):
    """ """

    homepage = "https://github.com/OP2/PyOP2"
    url      = "https://github.com/OP2/PyOP2"
    git='https://github.com/OP2/PyOP2'
    
    version('2019.05.29', tag='Firedrake_20190529.1')

    phases = ['build_ext', 'install']
    
    depends_on('py-setuptools', type="build")
    depends_on('py-pytest', type="build")
    depends_on('py-flake8', type="build")
    depends_on('py-decorator')
    depends_on('py-cython')
    depends_on('py-numpy')
    depends_on('py-mpi4py')
    depends_on('petsc@3.10:')
    depends_on('py-petsc4py')
    depends_on('firedrake.coffee')
    depends_on('firedrake.loopy')

    @run_before('build_ext')
    def fixme(self):
        filter_file(r'packages=\[\'pyop2\'\]', 'packages=[\'pyop2\',\'pyop2.codegen\']', 'setup.py')
        #with open('setup.py', 'r') as ff :
        #    print( ff.read() )
