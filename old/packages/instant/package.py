from spack import *

class Instant(Package):
    """Instant

Instant is a Python module that allows for instant inlining of C and
C++ code in Python. It is a small Python module built on top of SWIG
and Distutils.  Instant is part of the FEniCS Project.

For more information, visit http://www.fenicsproject.org.

    """

    homepage = "https://bitbucket.org/fenics-project/instant"
    url      = "https://bitbucket.org/fenics-project/instant/downloads/instant-2016.1.0.tar.gz"

    version('2016.1.0', git='https://bitbucket.org/fenics-project/instant', tag='instant-2016.1.0')
    version('1.7.0dev', git='https://bitbucket.org/fenics-project/instant', commit='406c1a85a8a90aa8a156a03b0e020abe035e056e')
    version('1.6.0', git='https://bitbucket.org/fenics-project/instant', tag='instant-1.6.0')
    

    extends('python')
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('cmake', type="run")
    depends_on('py-flufl_lock', type="run")
    depends_on('swig', type=("build","run"))
    
    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
