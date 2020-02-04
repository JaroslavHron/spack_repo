from spack import *

class Finat(PythonPackage):
    """FInAT is not a tabulator """

    homepage = "https://github.com/FInAT/FInAT"
    url      = "https://github.com/FInAT/FInAT"
    git='https://github.com/FInAT/FInAT'
   
    version('2019.12.31', commit='685bc3cde320f59463eab10307bb2e57af21edc5')
    version('2019.10.18', commit='685bc3cde320f59463eab10307bb2e57af21edc5')
    version('master', branch='master')

    #depends_on('py-setuptools', type="build")
    #depends_on('py-wheel', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-sympy', type=("build","run"))
