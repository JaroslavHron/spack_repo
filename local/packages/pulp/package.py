from spack import *

class Pulp(PythonPackage):
    """ """

    homepage = "https://github.com/coin-or/pulp"
    url      = "https://github.com/coin-or/pulp"
    git='https://github.com/coin-or/pulp'
    
    version('1.6.7', tag='1.6.7')

    depends_on('py-setuptools', type="build")
    
