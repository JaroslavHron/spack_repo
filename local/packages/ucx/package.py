# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ucx(AutotoolsPackage):
    """a communication library implementing high-performance messaging for
    MPI/PGAS frameworks"""

    homepage = "http://www.openucx.org"
    url      = "https://github.com/openucx/ucx/releases/download/v1.3.1/ucx-1.3.1.tar.gz"

    # Current
    version('1.7.0', sha256='6ab81ee187bfd554fe7e549da93a11bfac420df87d99ee61ffab7bb19bdd3371')
    version('1.6.1', sha256='1425648aa03f5fa40e4bc5c4a5a83fe0292e2fe44f6054352fbebbf6d8f342a1')
    version('1.6.0', sha256='360e885dd7f706a19b673035a3477397d100a02eb618371697c7f3ee4e143e2c')
    version('1.5.2', sha256='1a333853069860e86ba69b8d071ccc9871209603790e2b673ec61f8086913fad')
    version('1.5.1', sha256='567119cd80ad2ae6968ecaa4bd1d2a80afadd037ccc988740f668de10d2fdb7e')
    version('1.5.0', sha256='84f6e4fa5740afebb9b1c8bb405c07206e58c56f83120dcfcd8dc89e4b7d7458')
    version('1.4.0', sha256='99891a98476bcadc6ac4ef9c9f083bc6ffb188a96b3c3bc89c8bbca64de2c76e')

    # Still supported
    version('1.3.1', sha256='e058c8ec830d2f50d9db1e3aaaee105cd2ad6c1e6df20ae58b9b4179de7a8992')
    version('1.3.0', sha256='71e69e6d78a4950cc5a1edcbe59bf7a8f8e38d59c9f823109853927c4d442952')
    version('1.2.2', sha256='914d10fee8f970d4fb286079dd656cf8a260ec7d724d5f751b3109ed32a6da63')
    version('1.2.1', sha256='fc63760601c03ff60a2531ec3c6637e98f5b743576eb410f245839c84a0ad617')

    depends_on('numactl')
    depends_on('rdma-core')
    depends_on('binutils')

    def configure_args(self):
        spec = self.spec
        config_args = [
            '--enable-optimizations',
            '--enable-cma',
            '--enable-mt',
            '--with-verbs',
            '--without-java',
            '--disable-doxygen-doc'
        ]
        return(config_args)
