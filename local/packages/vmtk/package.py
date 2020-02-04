# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
from spack import *


class Vmtk(CMakePackage):
    """the Vascular Modeling Toolkit http://vmtk.org """

    homepage = "http://www.vmtk.org"
    url      = "http://www.vmtk.org"
    git      = "https://github.com/vmtk/vmtk.git"

    version('1.4.0', tag='v1.4.0')

    depends_on('python')
    depends_on('mesa')
    depends_on('cmake', type='build')

    extends('python')
    
    def install(self, spec, prefix):
        install_tree('spack-build/Install', prefix)

    def setup_environment(self, spack_env, run_env):
        # Set DIR in the module file
        run_env.set('VMTKHOME', self.prefix)
                                                                        
