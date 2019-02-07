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


class Mesa(Package):
    """Mesa is an open-source implementation of the OpenGL
    specification - a system for rendering interactive 3D graphics."""

    homepage = "http://www.mesa3d.org"
    url      = "ftp://ftp.freedesktop.org/pub/mesa"

    version('12.0.2', git='https://anongit.freedesktop.org/git/mesa/mesa.git', tag='mesa-12.0.2')
    
    depends_on("llvm", when='+llvm')
    depends_on("python")
    depends_on("libxml2+python")

    depends_on("py-mako")
    depends_on("flex", type='build')
    depends_on("bison", type='build')
    # depends_on("dri2proto")
    # depends_on("libxcb")
    # depends_on("libxshmfence")

    variant('llvm', default=True, description='Use llvm accelerated software renderer')
    variant('swrast', default=False, description='Build only software renderer')
    variant('gallium', default=False, description='Build only gallium software renderer')
    variant('oswr', default=False, description='Use OpenSWR software rasterizer')
    
    def install(self, spec, prefix):

        autoreconf = which("autoreconf")
        autoreconf("--install", "--verbose", "--force")

        config_args = ["PYTHON2=%s/python"%spec['python'].prefix.bin, \
                       "CXXFLAGS=-DDEFAULT_SOFTWARE_DEPTH_BITS=31", \
                       "CFLAGS=-DDEFAULT_SOFTWARE_DEPTH_BITS=31", \
                       "--prefix=%s" % prefix,\
                       "--disable-xvmc", \
                       "--enable-gl", \
                       "--enable-gles1", \
                       "--enable-gles2", \
                       "--enable-texture-float", \
                       "--enable-glx-tls", \
                       #"--disable-shared-glapi", \
                       "--disable-dri", \
                       "--disable-driglx-direct", \
                       "--disable-egl", \
                       "--with-egl-platforms="]

        config_args.extend(["--enable-gallium-llvm={0}".format("yes" if '+llvm' in spec else "no")])

        if '+swrast' in spec:
            config_args.extend([
                "--with-gallium-drivers=swrast", \
                "--enable-osmesa", \
                "--enable-glx=xlib", \
                "--with-dri-drivers=swrast"])
            

        if '+gallium' in spec:
            config_args.extend([
                "--with-gallium-drivers=swrast", \
                "--enable-gallium-osmesa", \
                "--enable-glx=gallium-xlib", \
                "--with-dri-drivers=swrast"])

        if '+oswr' in spec:
            config_args.extend([
                "--with-gallium-drivers=swr", \
                "--enable-osmesa", \
                "--enable-glx=xlib"])

        configure(*config_args)

        make()
        make("install")
