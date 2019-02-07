from spack import *

class Fiat(Package):
    """FIAT: FInite element Automatic Tabulator 

The FInite element Automatic Tabulator FIAT supports generation of
arbitrary order instances of the Lagrange elements on lines,
triangles, and tetrahedra. It is also capable of generating arbitrary
order instances of Jacobi-type quadrature rules on the same element
shapes. Further, H(div) and H(curl) conforming finite element spaces
such as the families of Raviart-Thomas, Brezzi-Douglas-Marini and
Nedelec are supported on triangles and tetrahedra. Upcoming versions
will also support Hermite and nonconforming elements.  FIAT is part of
the FEniCS Project.

For more information, visit http://www.fenicsproject.org

    """

    homepage = "https://bitbucket.org/fenics-project/fiat"
    url      = "https://bitbucket.org/fenics-project/fiat/downloads/fiat-2016.1.0.tar.gz"

    version('2016.1.0', git='https://bitbucket.org/fenics-project/fiat', tag='fiat-2016.1.0')
    version('1.7.0dev', git='https://bitbucket.org/fenics-project/fiat', commit='5b7f77abcea7d7e9b67b597a32543a12547ddf9b')
    version('1.6.0', git='https://bitbucket.org/fenics-project/fiat', tag='fiat-1.6.0')

    extends('python')
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-sympy', type=("build","run"))
    
    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
