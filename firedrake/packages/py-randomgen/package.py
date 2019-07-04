# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyRandomgen(PythonPackage):
    """randomgen"""

    homepage = "https://github.com/bashtage/randomgen"
    url      = "https://github.com/bashtage/randomgen/archive/v1.16.6.tar.gz"

    #version('1.17.0.dev0', sha256='56b3734a71e197c8f1d1c299ffb07fd080ba95d8582fbae29ff1e4aae907d878')
    version('1.16.6',      sha256='a2590f96a46c836c8f9923e04c4db1705e34b4421df351e9ba4292df51b0d692')
    version('1.16.5',      sha256='d93ee459d2557ef01d645f81005ca8d7d01f007aa59eb841acbd8f776f59809b')
    version('1.16.4',      sha256='45a995bc019e2511dc71d2af6ed3f1c9111f31fc2857dc6c134b455cae8260d5')
    version('1.16.3',      sha256='3f8d806e79d42f9c496425f815b2dde0ac01dd35d5b4018e75f013f14f6e8b05')
    version('1.16.2',      sha256='d989c7959f2b3e92d6a23c64ba1eab07335ada80adf96eb1c71a98e2b7846bf9')
    version('1.16.1',      sha256='019424666162b507077fc20f3d2801c4f82d042a5a88b16f13bf8d93392c4de9')
    version('1.16.0',      sha256='2944a7039d6e709f112cd2cde5558aa856b6b5bb26bd1d5d003af235efd7b543')
    version('1.15.1',      sha256='29203f91b910e569d3258363cd235b9f260cb8e0c8980f081f6bce32eb5c3891')
    version('1.15.0',      sha256='ff124868b0fc780d1db20174c4e2e4a6b04787ee6c1a5acb7559947672a77422')
                                        
    # FIXME: Add dependencies if required.
    depends_on('py-setuptools', type='build')
    depends_on('py-cython')
    depends_on('py-numpy')
