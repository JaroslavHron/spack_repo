from spack import *

class Tsfc(PythonPackage):
    """ """

    homepage = "https://github.com/firedrakeproject/tsfc"
    url      = "https://github.com/firedrakeproject/tsfc"
    git='https://github.com/firedrakeproject/tsfc'
    
    version('2019.05.29.1', tag='Firedrake_20190529.1')

    #depends_on('py-setuptools', type="build")
    depends_on('py-numpy')
    depends_on('firedrake.coffee')
    depends_on('firedrake.fiat')
    depends_on('firedrake.finat')
    depends_on('firedrake.ufl')

