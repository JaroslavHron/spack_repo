from spack import *

class Coffee(PythonPackage):
    """ """

    homepage = "https://github.com/coneoproject/COFFEE"
    url      = "https://github.com/coneoproject/COFFEE"
    git='https://github.com/coneoproject/COFFEE'
    
    version('2019.12.31', commit='72a4464aa18fd408de5304ac467db18d7af2b670')
    version('2019.10.18', commit='72a4464aa18fd408de5304ac467db18d7af2b670')
    version('master', branch='master')
    
    depends_on('py-setuptools', type="build")
    depends_on('pulp')
    depends_on('py-numpy')
    depends_on('py-networkx')
    depends_on('py-six')

