from spack import *

class Finat(PythonPackage):
    """FInAT is not a tabulator """

    homepage = "https://github.com/blechta/FInAT"
    url      = "https://github.com/blechta/FInAT"
    git='https://github.com/blechta/FInAT'
    
    version('2018.1.0', tag='2018.1.0')

    #depends_on('py-setuptools', type="build")
    #depends_on('py-wheel', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-sympy', type=("build","run"))
