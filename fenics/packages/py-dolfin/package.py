# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys
from spack import *


class PyDolfin(PythonPackage):
    """DOLFIN - python interface

    DOLFIN is the computational backend of FEniCS and implements the
    FEniCS Problem Solving Environment in Python and C++.

    """

    homepage = "https://bitbucket.org/fenics-project/dolfin"
    url      = "https://bitbucket.org/fenics-project/dolfin"
    git      = 'https://bitbucket.org/fenics-project/dolfin'
    
    version('2018.1.0', tag='2018.1.0.post2')

    depends_on('dolfin@2018.1.0')
    extends('python')

    # This are the build dependencies
    depends_on('py-setuptools')
    depends_on('py-bind11')
    depends_on('cmake')

    #python('setup.py', 'install', '--prefix={0}'.format(self.prefix))
    #def setup_environment(self, spack_env, run_env):
    #    spack_env.set('PYBIND11_USE_CMAKE', 1)

    def install(self, spec, prefix):
        super(PyDolfin, self).install(spec, prefix)
        setup_py('install', '--single-version-externally-managed', '--root=/', '--prefix={0}'.format(prefix))
        
