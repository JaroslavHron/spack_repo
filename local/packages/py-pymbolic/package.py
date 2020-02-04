# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPymbolic(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/inducer/pymbolic"
    url      = "https://github.com/inducer/pymbolic"
    git="https://github.com/inducer/pymbolic"

    # FIXME: Add proper versions and checksums here.
    version('2019.2', tag='v2019.2')
    version('2019.1', tag='v2019.1')
    version('2017.1', tag='v2017.1')

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    depends_on('py-pytools')
    depends_on('py-six')
    # depends_on('py-foo',        type=('build', 'run'))

