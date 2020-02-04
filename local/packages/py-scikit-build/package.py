# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyScikitBuild(PythonPackage):
    """Scikit-build"""

    homepage = "https://scikit-build.readthedocs.io"
    url      = "https://github.com/scikit-build/scikit-build/archive/0.10.0.tar.gz"

    version('0.10.0', sha256='2beec252813b20327072c15e9d997f15972aedcc6a130d0154979ff0fdb1b010')

    depends_on('python@2.7:2.8,3.4:', type=('build', 'run'))
    depends_on('py-setuptools@28.0.0:', type=('build', 'run'))
    depends_on('py-packaging', type=('build', 'run'))
    depends_on('py-wheel@0.29.0:', type=('build', 'run'))
    
    depends_on('py-coverage@4.2:', type='build')
    depends_on('py-cython@0.25.1:', type='build')
    depends_on('py-six@1.10.0:', type='build')
    depends_on('py-pytest@3.3.0:', type=('build','test'))
    depends_on('cmake')
