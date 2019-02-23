# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMpi4py(PythonPackage):
    """This package provides Python bindings for the Message Passing
       Interface (MPI) standard. It is implemented on top of the
       MPI-1/MPI-2 specification and exposes an API which grounds on the
       standard MPI-2 C++ bindings.
    """
    homepage = "https://pypi.python.org/pypi/mpi4py"
    url      = "https://pypi.io/packages/source/m/mpi4py/mpi4py-3.0.0.tar.gz"
    git      = "https://github.com/mpi4py/mpi4py.git"

    version('develop', branch='master')
    version('3.0.1', sha256='6549a5b81931303baf6600fa2e3bc04d8bd1d5c82f3c21379d0d64a9abcca851')
    version('3.0.0', 'bfe19f20cef5e92f6e49e50fb627ee70')
    version('2.0.0', '4f7d8126d7367c239fd67615680990e3')
    version('1.3.1', 'dbe9d22bdc8ed965c23a7ceb6f32fc3c')

    depends_on('python@2.7:2.8,3.3:')
    depends_on('py-setuptools', type='build')
    depends_on('mpi')
    depends_on('py-cython', when='@develop', type='build')

    @run_after('install')
    def post_install(self):
        self.setup_py('build_exe', '--mpi={0}'.format(self.spec['mpi'].prefix))
        self.setup_py('install_exe', '--install-dir={0}'.format(self.prefix))
        mkdirp(self.prefix.bin)
        symlink('../python3.6-mpi', '{0}/python-mpi'.format(self.prefix.bin))
                
