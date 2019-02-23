# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class BinBlender(Package):
    """ Blender is the free and open source 3D creation suite. """

    homepage = 'https://www.blender.org'
    url      = 'https://download.blender.org/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2'
    list_url = 'https://download.blender.org/release/Blender2.79'
    list_depth = 1
                    
    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.blender.org/"
    url      = "https://download.blender.org/release/Blender2.79/blender-2.79b-linux-glibc219-x86_64.tar.bz2"

    def url_for_version(self, version):
        url = "https://download.blender.org/release/Blender2.79/blender-{0}-linux-glibc219-x86_64.tar.bz2"
        return url.format(version)
    
    version('2.79b', sha256='43824a4e0b0c6de6fa34ff224eec44c1cc9f26a95f6f3c8c2558d1c05704183c', expand=False, preferred=True)
    version('2.79a', sha256='f84ac519ade1f6b015d97291bfdbe670427058acb621f06ba8cf4afd06fdce35', expand=False)
    version('2.79',  sha256='79e156acf2ec109fd0abb20f7f9bb16227e10fe5be4ed38b0674f4fe868fdd21', expand=False)
     
    def install(self, spec, prefix):
        Tar=Executable('tar')
        Tar('-x', '-a', '--directory', prefix, '--file', self.stage.archive_file)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', join_path(self.prefix))
