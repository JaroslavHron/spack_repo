from spack import *

class Pyop2(PythonPackage):
    """ """

    homepage = "https://github.com/OP2/PyOP2"
    url      = "https://github.com/OP2/PyOP2"
    git='https://github.com/OP2/PyOP2'
    
    version('2019.12.31', commit='8e1c5720fe0a8f7b4e870a49c43608d97c66ad14')
    version('2019.10.18', commit='070367eb5ffa3bacb5676b843eb77041c62a3066')
    version('master', branch='master')

    phases = ['build_ext', 'install']
    
    depends_on('py-setuptools', type="build")
    depends_on('py-pytest', type="build")
    depends_on('py-flake8', type="build")
    depends_on('py-decorator')
    depends_on('py-cython')
    depends_on('py-numpy')
    depends_on('py-mpi4py')
    
    #for v in [ '2019.12.31' , '2019.10.18' ] :
    #    depends_on('firedrake.petsc@trunk-firedrake.'+v, when='@'+v)
    #    depends_on('firedrake.py-petsc4py@trunk-firedrake.'+v, when='@'+v)

    #depends_on('firedrake.petsc@master-firedrake', when='@master')
    #depends_on('firedrake.py-petsc4py@master-firedrake', when='@master')

    depends_on('firedrake.petsc@master-firedrake')
    depends_on('firedrake.py-petsc4py@master-firedrake')

    depends_on('firedrake.coffee')
    depends_on('firedrake.coffee@master', when='@master')

    depends_on('firedrake.loopy')
    depends_on('firedrake.loopy@firedrake', when='@master')

    
    @run_before('build_ext')
    def fixme(self):
        filter_file(r'packages=\[\'pyop2\'\]', 'packages=[\'pyop2\',\'pyop2.codegen\']', 'setup.py')
        #with open('setup.py', 'r') as ff :
        #    print( ff.read() )
