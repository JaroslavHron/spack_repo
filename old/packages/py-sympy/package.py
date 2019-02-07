##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

class PySympy(Package):
    """SymPy is a Python library for symbolic mathematics."""
    homepage = "https://pypi.python.org/pypi/sympy"
    url      = "https://pypi.python.org/packages/source/s/sympy/sympy-0.7.6.tar.gz"

    version('0.7.6', '3d04753974306d8a13830008e17babca')
    version('1.0', '43e797de799f00f9e8fd2307dba9fab1')

    extends('python')
    depends_on('py-mpmath', when='@1.0:')

    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)
