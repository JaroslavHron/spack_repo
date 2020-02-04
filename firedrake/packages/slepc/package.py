# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import sys
from spack import *


class Slepc(Package):
    """Scalable Library for Eigenvalue Problem Computations."""

    homepage = "http://slepc.upv.es"
    url      = "http://slepc.upv.es/download/distrib/slepc-3.6.2.tar.gz"
    git      = "https://github.com/firedrakeproject/slepc"

    maintainers = ['joseeroman', 'balay']

    version('develop', branch='master')
    version('master-firedrake', branch='firedrake')

    #version('trunk-firedrake.2019.12.31', commit='5a5eed54fa55aa1a614efd75ac84e393850e961f', get_full_repo=True)
    #version('trunk-firedrake.2019.10.18', commit='5a5eed54fa55aa1a614efd75ac84e393850e961f', get_full_repo=True)

    version('3.12.0', sha256='872831d961cf76389fafb7553231ae1a6676555850c98ea0e893c06f596b2e9e')
    version('3.11.2', sha256='cd6a73ac0c9f689c12f2987000a7a28fa7df53fdc069fb59a2bb148699e741dd')
    version('3.11.1', sha256='4816070d4ecfeea6212c6944cee22dc7b4763df1eaf6ab7847cc5ac5132608fb')
    version('3.11.0', sha256='bf29043c311fe2c549a25e2b0835095723a3eebc1dff288a233b32913b5762a2')
    version('3.10.2', sha256='0594972293f6586458a54b7c1e1121b311a9c9449060355d52bb3bf09ad6812b')
    version('3.10.1', sha256='f64787c8c2ab3d2f6db3c67d2bfe6ee84f741ce3dfde1d2f8221e131820a12a1')
    version('3.10.0', sha256='069d7a579995e0be1567c5bc869251e29c00044369a786933ca3040149d0412a')
    version('3.9.2', sha256='247585b3f8c10bf50b9464cb8ef7b5f22bead6f96524384897a37ec4146eb03e')
    version('3.9.1', sha256='e174ea7c127d9161eef976b0288f0c56d443a58d6ab2dc8af1e8bd66f156ce17')
    version('3.9.0', sha256='1f3930db56b4065aaf214ea758ddff1a70bf19d45544cbdfd19d2787db4bfe0b')
    version('3.8.2', sha256='1e7d20d20eb26da307d36017461fe4a55f40e947e232739179dbe6412e22ed13')
    version('3.8.0', sha256='c58ccc4e852d1da01112466c48efa41f0839649f3a265925788237d76cd3d963')
    version('3.7.4', sha256='2fb782844e3bc265a8d181c3c3e2632a4ca073111c874c654f1365d33ca2eb8a')
    version('3.7.3', sha256='3ef9bcc645a10c1779d56b3500472ceb66df692e389d635087d30e7c46424df9')
    version('3.7.1', sha256='670216f263e3074b21e0623c01bc0f562fdc0bffcd7bd42dd5d8edbe73a532c2')
    version('3.6.3', sha256='384939d009546db37bc05ed81260c8b5ba451093bf891391d32eb7109ccff876')
    version('3.6.2', sha256='2ab4311bed26ccf7771818665991b2ea3a9b15f97e29fd13911ab1293e8e65df')

    variant('arpack', default=True, description='Enables Arpack wrappers')
    variant('blopex', default=False, description='Enables BLOPEX wrappers')

    # NOTE: make sure PETSc and SLEPc use the same python.
    depends_on('python@2.6:2.8', type='build', when='@:3.10.99')
    depends_on('python@2.6:2.8,3.4:', type='build', when='@3.11:')

    # Cannot mix release and development versions of SLEPc and PETSc:
    #depends_on('firedrake.petsc@trunk-firedrake.2019.12.31', when='@trunk-firedrake.2019.12.31')
    #depends_on('firedrake.petsc@trunk-firedrake.2019.10.18', when='@trunk-firedrake.2019.10.18')
    depends_on('firedrake.petsc@master-firedrake', when='@master-firedrake')
    depends_on('petsc@develop', when='@develop')
    depends_on('petsc@3.12:3.12.99', when='@3.12:3.12.99')
    depends_on('petsc@3.11:3.11.99', when='@3.11:3.11.99')
    depends_on('petsc@3.10:3.10.99', when='@3.10:3.10.99')
    depends_on('petsc@3.9:3.9.99', when='@3.9:3.9.99')
    depends_on('petsc@3.8:3.8.99', when='@3.8:3.8.99')
    depends_on('petsc@3.7:3.7.7', when='@3.7.1:3.7.4')
    depends_on('petsc@3.6.3:3.6.4', when='@3.6.2:3.6.3')
    depends_on('arpack-ng~mpi', when='+arpack^petsc~mpi~int64')
    depends_on('arpack-ng+mpi', when='+arpack^petsc+mpi~int64')

    #eigen needs cmake 
    depends_on('gmake')
    depends_on('cmake')

    patch('install_name_371.patch', when='@3.7.1')

    # Arpack can not be used with 64bit integers.
    conflicts('+arpack', when='^petsc+int64')

    resource(name='blopex',
             url='http://slepc.upv.es/download/external/blopex-1.1.2.tar.gz',
             sha256='0081ee4c4242e635a8113b32f655910ada057c59043f29af4b613508a762f3ac',
             destination=join_path('installed-arch-' + sys.platform + '-c-opt',
                                   'externalpackages'),
             when='+blopex')

    def install(self, spec, prefix):
        # set SLEPC_DIR for installation
        # Note that one should set the current (temporary) directory instead
        # its symlink in spack/stage/ !
        os.environ['SLEPC_DIR'] = os.getcwd()

        options = []

        if '+arpack' in spec:
            options.extend([
                '--with-arpack-dir=%s' % spec['arpack-ng'].prefix.lib,
            ])
            if 'arpack-ng~mpi' in spec:
                options.extend([
                    '--with-arpack-flags=-larpack'
                ])
            else:
                options.extend([
                    '--with-arpack-flags=-lparpack,-larpack'
                ])

        # It isn't possible to install BLOPEX separately and link to it;
        # BLOPEX has to be downloaded with SLEPc at configure time
        if '+blopex' in spec:
            options.append('--download-blopex')

        python('configure', '--prefix=%s' % prefix, *options)

        make('MAKE_NP=%s' % make_jobs, parallel=False)
        if self.run_tests:
            make('test', parallel=False)

        make('install', parallel=False)

    def setup_environment(self, spack_env, run_env):
        # configure fails if these env vars are set outside of Spack
        #spack_env.unset('PYTHONPATH')
        #spack_env.unset('PYTHONHOME')
        
        # Set SLEPC_DIR in the module file
        run_env.set('SLEPC_DIR', self.prefix)
        
    def setup_dependent_environment(self, spack_env, run_env, dependent_spec):
        # set up SLEPC_DIR for everyone using SLEPc package
        spack_env.set('SLEPC_DIR', self.prefix)
