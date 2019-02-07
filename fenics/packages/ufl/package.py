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

    homepage = "https://bitbucket.org/fenics-project/ufl"
    url      = "https://bitbucket.org/fenics-project/ufl/downloads/ufl-2017.2.0.tar.gz"
    git='https://bitbucket.org/fenics-project/ufl'

    version('2018.1.0', tag='2018.1.0')
    version('2017.2.0', tag='2017.2.0.post0')
    version('2017.1.0', tag='2017.1.0.post1')
    
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-six', type=("build","run"))
