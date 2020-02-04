from spack import *

class Tsfc(PythonPackage):
    """ """

    homepage = "https://github.com/firedrakeproject/tsfc"
    url      = "https://github.com/firedrakeproject/tsfc"
    git='https://github.com/firedrakeproject/tsfc'
    
    version('2019.12.31', commit='9bd9ec7020c0b0c8685c1ecd41a04e26593df12e')
    version('2019.10.18', commit='017ab494fb4366de0e429e7a92b5258f2191e915')
    version('master', branch='master')

    #depends_on('py-setuptools', type="build")
    depends_on('py-numpy')

    for p in ['coffee', 'fiat', 'finat', 'ufl'] :
        depends_on('firedrake.{0}'.format(p))
        depends_on('firedrake.{0}@master'.format(p), when='@master')

    depends_on('firedrake.coffee')                        
    depends_on('firedrake.fiat')
    depends_on('firedrake.finat')
    depends_on('firedrake.ufl')

