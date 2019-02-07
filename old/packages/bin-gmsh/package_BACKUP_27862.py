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


class Gmsh(Package):
    """Gmsh is a free 3D finite element grid generator with a built-in CAD engine
    and post-processor. Its design goal is to provide a fast, light and
    user-friendly meshing tool with parametric input and advanced visualization
    capabilities. Gmsh is built around four modules: geometry, mesh, solver and
    post-processing. The specification of any input to these modules is done
    either interactively using the graphical user interface or in ASCII text
    files using Gmsh's own scripting language.
    """

    homepage = 'http://gmsh.info'
    url = 'http://gmsh.info'

    def url_for_version(self, version):
        return 'http://gmsh.info/bin/Linux/gmsh-{0}-Linux64.tgz'.format(version)
    
    
    version('2.13.1', '9ddd236b74669af88035addb3b7cb007')
      
    def install(self, spec, prefix):
<<<<<<< HEAD
        install_tree(join_path(self.stage.source_path,'bin'), join_path(prefix,'bin'))
        install_tree(join_path(self.stage.source_path,'share'), join_path(prefix,'share'))
=======
        options = []
        options.extend(std_cmake_args)

        # Make sure native file dialogs are used
        options.extend(['-DENABLE_NATIVE_FILE_CHOOSER=ON'])

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        options.append('-DCMAKE_INSTALL_NAME_DIR:PATH=%s/lib' % prefix)

        # Prevent GMsh from using its own strange directory structure on OSX
        options.append('-DENABLE_OS_SPECIFIC_INSTALL=OFF')

        # Make sure GMSH picks up correct BlasLapack by providing linker flags
        blas_lapack = spec['lapack'].lapack_libs + spec['blas'].blas_libs
        options.append(
            '-DBLAS_LAPACK_LIBRARIES={0}'.format(blas_lapack.ld_flags))

        # Gmsh does not have an option to compile against external metis.
        # Its own Metis, however, fails to build
        options.append('-DENABLE_METIS=OFF')

        if '+fltk' in spec:
            options.append('-DENABLE_FLTK=ON')
        else:
            options.append('-DENABLE_FLTK=OFF')

        if '+oce' in spec:
            env['CASROOT'] = self.spec['oce'].prefix
            options.extend(['-DENABLE_OCC=ON'])
        else:
            options.extend(['-DENABLE_OCC=OFF'])

        if '+petsc' in spec:
            env['PETSC_DIR'] = self.spec['petsc'].prefix
            options.extend(['-DENABLE_PETSC=ON'])
        else:
            options.extend(['-DENABLE_PETSC=OFF'])

        if '+slepc' in spec:
            env['SLEPC_DIR'] = self.spec['slepc'].prefix
            options.extend(['-DENABLE_SLEPC=ON'])
        else:
            options.extend(['-DENABLE_SLEPC=OFF'])

        if '+shared' in spec:
            # Builds dynamic executable and installs shared library
            options.extend(['-DENABLE_BUILD_SHARED:BOOL=ON',
                            '-DENABLE_BUILD_DYNAMIC:BOOL=ON'])
        else:
            # Builds and installs static library
            options.append('-DENABLE_BUILD_LIB:BOOL=ON')

        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug')

        if '+mpi' in spec:
            options.append('-DENABLE_MPI:BOOL=ON')

        if '+compression' in spec:
            options.append('-DENABLE_COMPRESSED_IO:BOOL=ON')
>>>>>>> upstream/develop

