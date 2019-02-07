# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fenics(Package):
    """FEniCS is a popular open-source (LGPLv3) computing platform for solving partial differential equations (PDEs)."""

    homepage = "https://fenicsproject.org/"
    url      = "https://bitbucket.org/fenics-project/fenics"
    git      = 'https://bitbucket.org/fenics-project/fenics'

    version('2018.1.0', tag='2018.1.0')
    version('2017.2.0', tag='2017.2.0')

    depends_on('dolfin@2018.1.0', when='@2018.1.0')
    depends_on('mshr@2018.1.0', when='@2018.1.0')

    depends_on('dolfin@2017.2.0', when='@2017.2.0')
    depends_on('mshr@2017.2.0', when='@2017.2.0')

    def install(self, spec, prefix):
        install('README.rst', prefix)
    
                            
