from spack import *

class Finat(PythonPackage):
    """FInAT is not a tabulator """

    homepage = "https://github.com/FInAT/FInAT"
    url      = "https://github.com/FInAT/FInAT"
    git='https://github.com/FInAT/FInAT'
    
    version('2019.05.29', tag='Firedrake_20190529.1')

    #depends_on('py-setuptools', type="build")
    #depends_on('py-wheel', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-sympy', type=("build","run"))
