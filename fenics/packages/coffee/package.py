from spack import *

class Coffee(PythonPackage):
    """ """

    homepage = "https://github.com/blechta/COFFEE"
    url      = "https://github.com/blechta/COFFEE"
    git='https://github.com/blechta/COFFEE'
    
    version('2018.1.0', tag='2018.1.0')

    #PuLP
    #networkx
    #numpy
    #six
    
    depends_on('py-setuptools', type="build")
    depends_on('pulp')
    depends_on('py-numpy')
    depends_on('py-networkx')
    depends_on('py-six')

