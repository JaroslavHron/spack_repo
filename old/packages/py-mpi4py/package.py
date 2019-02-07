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

class PyMpi4py(Package):
    """This package provides Python bindings for the Message Passing Interface (MPI) standard. It is implemented on top of the MPI-1/MPI-2 specification and exposes an API which grounds on the standard MPI-2 C++ bindings."""
    homepage = "https://pypi.python.org/pypi/mpi4py"
    url      = "https://bitbucket.org/mpi4py/"

    version('1.3.1', git='https://bitbucket.org/mpi4py/mpi4py.git', tag='1.3.1')
    version('2.0.0', git='https://bitbucket.org/mpi4py/mpi4py.git', tag='2.0.0')

    extends('python')
    depends_on('python')
    depends_on('py-setuptools', type='build')
    depends_on('py-cython', type='build')
    depends_on('mpi')
    depends_on('py-numpy')

    def install(self, spec, prefix):
        with open('mpi.cfg', 'w') as f:
            f.write('[mpi]\n')
            f.write('mpi_dir={0}\n'.format(spec['mpi'].prefix))
            f.write('libraries={0} {1}\n'.format('mpi','open-pal'))
            f.write('include_dirs={0}\n'.format(spec['mpi'].prefix.include))
            f.write('library_dirs={0}\n'.format(spec['mpi'].prefix.lib))
            #f.write('runtime_library_dirs={0}\n'.format(spec['mpi'].prefix.lib))
            #f.write('rpath={0}\n'.format(spec['mpi'].prefix.lib))
            #f.write('extra_compile_args   = -L{0}\n'.format(spec['mpi'].prefix.lib))
            #f.write('extra_link_args      = -L{0}\n'.format(spec['mpi'].prefix.lib))
            #f.write('extra_objects        =\n')
            
        python('setup.py', 'build', '--mpi=mpi') #, '--configure')
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
