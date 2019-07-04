# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyIslpy(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/inducer/islpy"
    url      = "https://github.com/inducer/islpy"
    git="https://github.com/inducer/islpy"

    # FIXME: Add proper versions and checksums here.
    version('master', branch='master', submodules=True )

    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    depends_on('py-pytest')
    depends_on('py-cffi')
    depends_on('py-six')

    #depends_on('isl')
    #depends_on('imath')
    
    # depends_on('py-foo',        type=('build', 'run'))
