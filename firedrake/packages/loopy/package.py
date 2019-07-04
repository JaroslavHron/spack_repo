# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Loopy(PythonPackage):
    """loopy"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/firedrakeproject/loopy"
    url      = "https://github.com/firedrakeproject/loopy"
    git = "https://github.com/firedrakeproject/loopy"

    version('master', branch='master' , submodules=True )
    version('2019.05.29', tag='Firedrake_20190529.1', submodules=True)
     
    depends_on('py-setuptools', type='build')
    depends_on('py-pytools')
    depends_on('py-pymbolic')
    depends_on('py-cgen')
    depends_on('py-genpy')
    depends_on('py-codepy')
    depends_on('py-mako')
    #depends_on('py-f2py')
    #depends_on('py-pyopencl')
    depends_on('py-islpy')

    depends_on('py-ply')
