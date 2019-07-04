# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGenpy(PythonPackage):
    """genpy"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/inducer/genpy"
    url      = "https://github.com/inducer/genpy"
    git="https://github.com/inducer/genpy"

    # FIXME: Add proper versions and checksums here.
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    # depends_on('py-setuptools', type='build')
    depends_on('py-pytools')
    depends_on('py-numpy')
