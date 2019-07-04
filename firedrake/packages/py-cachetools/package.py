# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCachetools(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/tkem/cachetools"
    url      = "https://github.com/tkem/cachetools/archive/v3.1.1.tar.gz"
    git = "https://github.com/tkem/cachetools"

    version('3.1.0', sha256='9863c750b563850db89c73332b8f7b92ec8de03050daf396b84d89b48fb009e3')
    version('3.1.1', sha256='01ee1c1a94ece91cd18f5b2175156fd9089830e78f7c4241ab84cd3315bd60d1')
        
    depends_on('py-setuptools', type='build')
    
