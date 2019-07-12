# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libspatialindex(CMakePackage):
    homepage = "http://libspatialindex.github.io"
    url      = "https://github.com/firedrakeproject/libspatialindex"
    git = "https://github.com/firedrakeproject/libspatialindex"

    version('master', branch='master' )

    #@property
    #def libs(self):
    #    return find_libraries(
    #        ['libspatialindex'], root=self.prefix, recursive=True, shared=shared
    #        )
