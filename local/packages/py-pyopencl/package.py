# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-pyopencl
#
# You can edit this file again by typing:
#
#     spack edit py-pyopencl
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPyopencl(PythonPackage):
    """pyopencl"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/inducer/pyopencl"
    url      = "https://github.com/inducer/pyopencl"
    git = "https://github.com/inducer/pyopencl"

    # FIXME: Add proper versions and checksums here.
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    # depends_on('py-setuptools', type='build')
    depends_on('py-numpy')
    depends_on('py-pytools')
    depends_on('py-pybind11')
    depends_on('py-decorator')
    depends_on('py-appdirs')
    depends_on('py-six')
    depends_on('py-mako')

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
