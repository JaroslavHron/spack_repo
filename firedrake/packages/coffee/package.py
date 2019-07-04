from spack import *

class Coffee(PythonPackage):
    """ """

    homepage = "https://github.com/coneoproject/COFFEE"
    url      = "https://github.com/coneoproject/COFFEE"
    git='https://github.com/coneoproject/COFFEE'
    
    version('2019.05.29', tag='Firedrake_20190529.1')
    
    depends_on('py-setuptools', type="build")
    depends_on('pulp')
    depends_on('py-numpy')
    depends_on('py-networkx')
    depends_on('py-six')

