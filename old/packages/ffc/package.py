from spack import *
import os

class Ffc(Package):
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

    version('2016.1.0', git='https://bitbucket.org/fenics-project/ffc', tag='ffc-2016.1.0')
    version('1.7.0dev', git='https://bitbucket.org/fenics-project/ffc', commit='3ac2dad202525b5e7cb04b17c9c1f5df716334bd')
    version('1.6.0', git='https://bitbucket.org/fenics-project/ffc', tag='ffc-1.6.0')
    
    depends_on('swig')

    extends('python')
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-six', type=("build","run"))

    for ver in ['@2016.1.0','@1.7.0dev','@1.6.0'] :
        depends_on('fiat{0}'.format(ver), type=("build","run"), when=ver)
        depends_on('instant{0}'.format(ver), type=("build","run"), when=ver)
        depends_on('ufl{0}'.format(ver), type=("build","run"), when=ver)
    
    def install(self, spec, prefix):
        os.environ['SWIG'] = join_path(spec['swig'].prefix, 'bin', 'swig')
        os.environ['SWIG_EXECUTABLE'] = join_path(spec['swig'].prefix, 'bin', 'swig')
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
