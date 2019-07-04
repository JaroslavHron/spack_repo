from spack import *

class Tsfc(PythonPackage):
    """ """

    homepage = "https://github.com/blechta/tsfc"
    url      = "https://github.com/blechta/tsfc"
    git='https://github.com/blechta/tsfc'
    
    version('2018.1.0', tag='2018.1.0')

    #depends_on('py-setuptools', type="build")
    depends_on('py-numpy')
    depends_on('fenics.coffee@2018.1.0')
    depends_on('fenics.fiat@2018.1.0')
    depends_on('fenics.finat@2018.1.0')
    depends_on('fenics.ufl@2018.1.0')

