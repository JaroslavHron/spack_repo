from spack import *

class Dijitso(PythonPackage):
    """dijitso

A Python module for distributed just-in-time shared library building

For more information, visit http://www.fenicsproject.org.

    """

    homepage = "https://bitbucket.org/fenics-project/dijitso"
    url      = "https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-2017.2.0.tar.gz"
    git='https://bitbucket.org/fenics-project/dijitso'
    
    version('2019.1.0', tag='2019.1.0')
    version('2018.1.0', tag='2018.1.0')
    version('2017.2.0', tag='2017.2.0')
    version('2017.1.0', tag='2017.1.0.post1')
    
    depends_on('py-setuptools', type="build")
