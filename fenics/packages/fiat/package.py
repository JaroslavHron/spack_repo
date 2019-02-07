from spack import *

class Fiat(PythonPackage):
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
    url      = "https://bitbucket.org/fenics-project/fiat/downloads/fiat-2017.2.0.tar.gz"
    git='https://bitbucket.org/fenics-project/fiat'
    
    version('2018.1.0', tag='2018.1.0')
    version('2017.2.0', tag='2017.2.0')
    version('2017.1.0', tag='2017.1.0.post1')

    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-sympy', type=("build","run"))
