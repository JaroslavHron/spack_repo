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

class PySphinx(Package):
    """Sphinx Documentation Generator."""
    homepage = "http://sphinx-doc.org"
    url      = "https://pypi.python.org/packages/source/S/Sphinx/Sphinx-1.3.1.tar.gz"

    version('1.3.1', '8786a194acf9673464c5455b11fd4332')

    extends('python')
    depends_on('py-six')
    depends_on('py-docutils')
    
    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix=%s' % prefix)

    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        spack_env.set('SPHINX_DIR', self.prefix)
