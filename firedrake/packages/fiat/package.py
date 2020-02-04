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

    homepage = "https://github.com/firedrakeproject/fiat"
    url      = "https://github.com/firedrakeproject/fiat"
    git='https://github.com/firedrakeproject/fiat'
    
    version('2019.12.31', commit='ae587ff3a32be0b23edae3222e88b0f62da9f3e4')
    version('2019.10.18', commit='ae587ff3a32be0b23edae3222e88b0f62da9f3e4')
    version('master', branch='master')

    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-sympy', type=("build","run"))
