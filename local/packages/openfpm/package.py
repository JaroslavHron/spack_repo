# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
from spack import *


class Openfpm(CMakePackage):
    """OPEN FRAMEWORK FOR PARTICLES AND MESH SIMULATIONS """

    homepage = "http://openfpm.mpi-cbg.de/"
    url      = "http://openfpm.mpi-cbg.de/"
    git      = "https://github.com/IBirdSoft/openfpm_pdata_2.0.0.git"

    version('2.0.0', tag='master', submodules=True)

    depends_on('cmake', type='build')
    depends_on('python')
    depends_on('mpi')
    depends_on('metis')
    depends_on('parmetis')
    depends_on('boost')
    depends_on('lapack')
    depends_on('suite-sparse')
    depends_on('eigen')
    depends_on('hdf5')
    #depends_on('libhilbert')

    #cd openfpm_pdata_2.0.0 && ./install -d -c "--prefix=/where/you/want/to/install" && make install
    
    #def install(self, spec, prefix):
    #    shell('install', '-d', '-c', '--prefix='+prefix)
    #    make('install')
    #    #install_tree('spack-build/Install', prefix)
