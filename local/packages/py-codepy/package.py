# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCodepy(PythonPackage):
    """codepy"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/inducer/codepy"
    url      = "https://github.com/inducer/codepy"
    git="https://github.com/inducer/codepy"

    # FIXME: Add proper versions and checksums here.
    version('master', branch='master')

    # FIXME: Add dependencies if required.
    # depends_on('py-setuptools', type='build')
    depends_on('py-pytools')
    depends_on('py-numpy')
    depends_on('py-appdirs')
    depends_on('py-six')
    depends_on('py-cgen')
