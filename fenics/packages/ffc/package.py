from spack import *
import os

class Ffc(PythonPackage):
    """FFC: The FEniCS Form Compiler

FFC is a compiler for finite element variational forms. From a
high-level description of the form, it generates efficient low-level
C++ code that can be used to assemble the corresponding discrete
operator (tensor). In particular, a bilinear form may be assembled
into a matrix and a linear form may be assembled into a vector. FFC
may be used either from the command line (by invoking the ffc command)
or as a Python module (import ffc).  FFC is part of the FEniCS
Project.

For more information, visit http://www.fenicsproject.org
    """

    homepage = "https://bitbucket.org/fenics-project/ffc"
    url      = "https://bitbucket.org/fenics-project/ffc/downloads/ffc-2016.1.0.tar.gz"
    git='https://bitbucket.org/fenics-project/ffc'

    version('2018.1.0', tag='2018.1.0.post0')
    version('2017.2.0', tag='2017.2.0.post0')
    version('2017.1.0', tag='2017.1.0.post2')
    
    depends_on('swig')

    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-six', type=("build","run"))

    for ver in ['2018.1.0','2017.2.0','2017.1.0'] :
        wver='@'+ver
        depends_on('fiat{0}'.format(wver), type=("build","run"), when=wver)
        if( Version(ver) < Version('2018.1.0') ) :
            depends_on('instant{0}'.format(wver), type=("build","run"), when=wver)
        depends_on('ufl{0}'.format(wver), type=("build","run"), when=wver)
