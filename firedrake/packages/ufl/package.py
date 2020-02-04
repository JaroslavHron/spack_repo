from spack import *

class Ufl(PythonPackage):
    """UFL - Unified Form Language

The Unified Form Language (UFL) is a domain specific language for
declaration of finite element discretizations of variational
forms. More precisely, it defines a flexible interface for choosing
finite element spaces and defining expressions for weak forms in a
notation close to mathematical notation.  UFL is part of the FEniCS
Project.

For more information, visit http://www.fenicsproject.org

    """

    homepage = "https://github.com/firedrakeproject/ufl"
    url      = "https://github.com/firedrakeproject/ufl"
    git='https://github.com/firedrakeproject/ufl'

    version('2019.12.31', commit='afcc31c0e5fcdb4ddda8560e1be7a8c8b086837d')
    version('2019.10.18', commit='afcc31c0e5fcdb4ddda8560e1be7a8c8b086837d')
    version('master', branch='master')
    
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-six', type=("build","run"))
