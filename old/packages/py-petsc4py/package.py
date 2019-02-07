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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-petsc4py
#
# You can edit this file again by typing:
#
#     spack edit py-petsc4py
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyPetsc4py(Package):
    """Petsc4py are python interface to PETSc library."""
    homepage = "https://bitbucket.org/petsc/petsc4py"
    url      = "https://bitbucket.org/petsc/petsc4py"

    version('3.7.0', git='https://bitbucket.org/petsc/petsc4py.git', tag='3.7.0')
    extends('python')
    
    depends_on('py-cython', type='build')
    depends_on('py-mpi4py')
    depends_on('py-numpy')
    depends_on('petsc@3.7:3.7.99', when='@3.7:3.7.99')
    depends_on('petsc@3.6:3.6.99', when='@3.6:3.6.99')
    depends_on('petsc@3.5:3.5.99', when='@3.5:3.5.99')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
