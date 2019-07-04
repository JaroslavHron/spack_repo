# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPytools(PythonPackage):
    """pytools"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/inducer/pytools"
    url      = "https://github.com/inducer/pytools"
    git = "https://github.com/inducer/pytools"

    version('2019.1.1', tag='v2019.1.1')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    depends_on('py-decorator')
    depends_on('py-appdirs')
    depends_on('py-six')
    depends_on('py-numpy')
    # depends_on('py-foo',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
