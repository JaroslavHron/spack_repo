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

import os
import shutil
import glob
from spack import *


class Gap(Package):
    """GAP - Groups, Algorithms, Programming, a System for Computational Discrete Algebra"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.gap-system.org"
    url      = "https://github.com/gap-system/gap/archive/v4.8.4.tar.gz"

    version('4.8.4', '7621fba485ef190ad3d838abf810670a')
    version('4.8.3', 'ee8cf64fd0522237387f36dcd4328eb3')
    version('4.8.2', '8883afdea33a45e8539ce14dd78f620a')
    version('4.8.1', '8b019fa35476c2ce6140ea4f72e83673')
    version('4.8.0', 'cd2aaac5fcfc90c2406759963cf27a73')
    version('4.7.9', 'af1cdb5697388c88f1bc7a907ffbf1f7')
    version('4.7.8', 'd6e14afa300930653f9273d385e7690a')
    version('4.7.7', '853af1c77e77c4dc05db35762528ad9c')

    depends_on('gmp')
    depends_on('readline')

    def install(self, spec, prefix):
        with working_dir('.'):
            for f in glob.glob('*'):
                if os.path.isdir(f):
                    shutil.copytree(f, os.path.join(prefix, f))
                else:
                    shutil.copy2(f, os.path.join(prefix, f))

        bash = which('bash')
        cfg=['--with-gmp=system', '--with-readline={0}'.format(spec['readline'].prefix)]
        with working_dir(prefix):
            configure(*cfg)
            make()
            make('bootstrap-pkg-full')            
            with working_dir('pkg') :
                bash('../bin/BuildPackages.sh')
    
