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
import platform


class PyNumpy(Package):
    """NumPy is the fundamental package for scientific computing with Python.
    It contains among other things: a powerful N-dimensional array object,
    sophisticated (broadcasting) functions, tools for integrating C/C++ and
    Fortran code, and useful linear algebra, Fourier transform, and random
    number capabilities"""
    homepage = "http://www.numpy.org/"
    url      = "https://pypi.python.org/packages/source/n/numpy/numpy-1.9.1.tar.gz"

    version('1.11.0', 'bc56fb9fc2895aa4961802ffbdb31d0b')
    version('1.10.4', 'aed294de0aa1ac7bd3f9745f4f1968ad')
    version('1.9.2',  'a1ed53432dbcd256398898d35bc8e645')
    version('1.9.1',  '78842b73560ec378142665e712ae4ad9')

    variant('blas',   default=True)
    variant('lapack', default=True)

    extends('python')
    depends_on('py-nose', type='build')
    depends_on('py-setuptools', type='build')
    depends_on('blas',   when='+blas')
    depends_on('lapack', when='+lapack')

    def setup_dependent_package(self, module, dep_spec):
        python_version = self.spec['python'].version.up_to(2)
        arch = '{0}-{1}'.format(platform.system().lower(), platform.machine())

        self.spec.include = join_path(
            self.prefix.lib,
            'python{0}'.format(python_version),
            'site-packages',
            'numpy-{0}-py{1}-{2}.egg'.format(
                self.spec.version, python_version, arch),
            'numpy/core/include')

    def install(self, spec, prefix):
        libraries    = []
        library_dirs = []

        if '+blas' in spec:
            libraries.append('blas')
            library_dirs.append(spec['blas'].prefix.lib)
        if '+lapack' in spec:
            libraries.append('lapack')
            library_dirs.append(spec['lapack'].prefix.lib)

        if '+blas' in spec or '+lapack' in spec:
            with open('site.cfg', 'w') as f:
                f.write('[DEFAULT]\n')
                f.write('libraries=%s\n'    % ','.join(libraries))
                f.write('library_dirs=%s\n' % ':'.join(library_dirs))
                f.write('rpath=%s\n' % ':'.join(library_dirs))

        python('setup.py', 'install', '--prefix=%s' % prefix)
