# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Libsupermesh(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://bitbucket.org/libsupermesh/libsupermesh"
    url      = "https://bitbucket.org/libsupermesh/libsupermesh/downloads/libsupermesh-1.0.1.tar.gz"
    git = "https://bitbucket.org/libsupermesh/libsupermesh"

    #version('1.0.1', sha256='5b263b12346f12eed45022b351562bcdf0e290a40ea725731b96840d42b7cbe2')
    #version('1.0.0', sha256='f4ac6abef209b3a08a9355a01e41f9b3bea0d2b22ca44e09e17c502f790535ff')

    version('master', branch='master')

            
    
    depends_on('mpi')
    #depends_on('judy')

    def cmake_args(self):
        spec = self.spec
        
        opts = [
            "-DBUILD_SHARED_LIBS:BOOL=ON",
            "-DMPI_C_COMPILER={}".format(spec['mpi'].mpicc),
            "-DMPI_CXX_COMPILER={}".format(spec['mpi'].mpicxx),
            "-DMPI_Fortran_COMPILER={}".format(spec['mpi'].mpifc)
        ]
        
        return(opts)
    
    
