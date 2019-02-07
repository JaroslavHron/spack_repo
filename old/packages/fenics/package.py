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
import sys
from spack import *

class Fenics(Package):
    """FEniCS is organized as a collection of interoperable components
    that together form the FEniCS Project. These components include
    the problem-solving environment DOLFIN, the form compiler FFC, the
    finite element tabulator FIAT, the just-in-time compiler Instant,
    the code generation interface UFC, the form language UFL and a
    range of additional components."""

    homepage = "http://fenicsproject.org/"
    url      = "https://bitbucket.org/fenics-project"

    #version('2016.1.0', git='https://bitbucket.org/fenics-project/dolfin', tag='dolfin-2016.1.0')
    #version('1.7.0dev', git='https://bitbucket.org/fenics-project/dolfin', commit='c119915a877bf543e139f159274aad19a796d2a2')
    #version('1.6.0', git='https://bitbucket.org/fenics-project/dolfin', tag='dolfin-1.6.0')

    #res=[ 'ufl', 'fiat', 'instant', 'ffc', 'mshr']
    #for i in res :
    #    resource(name=i, \
    #             url='https://bitbucket.org/fenics-project/{0}'.format(i), \
    #             tag='{0}-2016.1.0'.format(i), \
    #             when='@2016.1.0', placement=i)


    releases = {
        '2016.1.0': {
            'dolfin': {'tag': 'dolfin-2016.1.0'},
            'resources': {
                'instant': {'tag': 'instant-2016.1.0'},
                'ffc': {'tag': 'ffc-2016.1.0'},
                'fiat': {'tag': 'fiat-2016.1.0'},
                'ufl': {'tag': 'ufl-2016.1.0'},
                'mshr': {'tag': 'mshr-2016.1.0'}
            },
        },
        '1.6.0': {
            'dolfin': {'tag': 'dolfin-1.6.0'},
            'resources': {
                'instant': {'tag': 'instant-1.6.0'},
                'ffc': {'tag': 'ffc-1.6.0'},
                'fiat': {'tag': 'fiat-1.6.0'},
                'ufl': {'tag': 'ufl-1.6.0'},
                'uflacs-deprecated': {'tag': 'uflacs-1.6.0'},
                'mshr': {'tag': 'mshr-1.6.0'}
            }
        },
        '1.7.0dev': {
            'dolfin': {'branch': 'jan/fix-slow-real'},
            'resources': {
                'instant': {'commit': '406c1a85a8a90aa8a156a03b0e020abe035e056e'},
                'ffc': {'commit': '3ac2dad202525b5e7cb04b17c9c1f5df716334bd'},
                'fiat': {'commit': '5b7f77abcea7d7e9b67b597a32543a12547ddf9b'},
                'ufl': {'commit': 'f3d31f2aea32141b2789a42839d0b22d188b6f2a'},
                'uflacs-deprecated': {'commit': '073fd2bb24bef7929bf6c12b55b78904311a9245'},
                'mshr': {'commit': '6e7cd5cd80e2d0c5c3040b19ac9f08b506be6727'}
            }
        }
    }
    
    
    for ver, release in releases.items():
        version(ver, **dict(release['dolfin'], **{'git': 'https://bitbucket.org/fenics-project/dolfin'}))
        for name, tag in release['resources'].items():
            resource(**dict(tag, **{'name': name, 'git': 'https://bitbucket.org/fenics-project/{0}'.format(name), 'when': '@{0}'.format(ver), 'placement': name}))
            
        
    variant('petsc',        default=True,  description='Compile with PETSc')
    variant('hdf5',         default=True,  description='Compile with HDF5')
    variant('scotch',       default=True,  description='Compile with Scotch')
    variant('slepc',        default=True,  description='Compile with SLEPc')
    variant('trilinos',     default=True,  description='Compile with Trilinos')
    variant('suitesparse',  default=True,  description='Compile with SuiteSparse solvers')
    variant('vtk',          default=True, description='Compile with VTK')
    variant('mpi',          default=True,  description='Enables the distributed memory support')
    variant('shared',       default=True,  description='Enables the build of shared libraries')
    variant('debug',        default=False, description='Builds a debug version of the libraries')

    variant('mpi4py',     default=True,  description='Uses mpi4py')
    variant('petsc4py',     default=True,  description='Uses PETSc4py')
    variant('slepc4py',     default=True,  description='Uses SLEPc4py')

    variant('pastix',       default=False,  description='Compile with Pastix')

    variant('doc',     default=True,  description='Create docs.')
    
    #patch('petsc-3.7.patch', when='^petsc@3.7:')
    #patch('petsc-version-detection.patch')

    extends('python')

    depends_on('python@2.6:2.7')

    depends_on('py-mpi4py', when='+mpi')
    depends_on('petsc@3.7:', when='+petsc')
    depends_on('slepc@3.7:', when='+slepc')
    depends_on('py-petsc4py', when='+petsc4py')
    depends_on('py-slepc4py', when='+slepc4py')
    depends_on('py-numpy')
    depends_on('py-sympy')
    depends_on('py-ply')
    depends_on('py-six')
    depends_on('py-matplotlib')
    depends_on('py-sphinx@1.0.1:', when='+doc')
    depends_on('eigen@3.2.0:')
    depends_on('boost')
    depends_on('gmp')
    depends_on('mpfr')
    depends_on('mpi', when='+mpi')
    depends_on('hdf5', when='+hdf5')
    depends_on('scotch', when='+scotch')
    depends_on('trilinos', when='+trilinos')
    depends_on('vtk+opengl2+sw', when='+vtk')
    depends_on('suite-sparse', when='+suitesparse')

    # This are the build dependencies
    depends_on('py-setuptools')
    depends_on('cmake@2.8.12:')
    depends_on('swig')

    def cmake_is_on(self, option):
        return 'ON' if option in self.spec else 'OFF'

    def install(self, spec, prefix):
        os.environ['CC'] = spec['mpi'].mpicc
        os.environ['CXX'] = spec['mpi'].mpicxx
        os.environ['F77'] = spec['mpi'].mpif77
        os.environ['FC'] = spec['mpi'].mpifc

        os.environ['PETSC_DIR'] = spec['petsc'].prefix
        os.environ['MPFR_DIR'] = spec['mpfr'].prefix
        os.environ['SPHINX_DIR'] = spec['py-sphinx'].prefix
        os.environ['HDF5_DIR'] = spec['hdf5'].prefix
        
        for package in ['ufl', 'ffc', 'fiat', 'instant']:
            with working_dir(package):
                python('setup.py', 'install', '--prefix={0}'.format(prefix))
            
        cmake_args = [
            '-DCMAKE_BUILD_TYPE:STRING={0}'.format('Debug' if '+debug' in spec else 'Release'),
            '-DBUILD_SHARED_LIBS:BOOL={0}'.format(self.cmake_is_on('+shared')),
            '-DDOLFIN_SKIP_BUILD_TESTS:BOOL=OFF',
            '-DDOLFIN_AUTO_DETECT_MPI:BOOL=OFF',
            '-DCMAKE_USE_RELATIVE_PATHS:BOOL=ON',
            '-DPYTHON_EXECUTABLE:FILEPATH={0}/python'.format(spec['python'].prefix.bin),
            '-DDOLFIN_ENABLE_OPENMP:BOOL=OFF',
            '-DDOLFIN_ENABLE_CHOLMOD:BOOL={0}'.format(self.cmake_is_on('suite-sparse')),
            '-DDOLFIN_ENABLE_HDF5:BOOL={0}'.format(self.cmake_is_on('hdf5')),
            '-DDOLFIN_ENABLE_MPI:BOOL={0}'.format(self.cmake_is_on('+mpi')),
            '-DDOLFIN_ENABLE_PARMETIS:BOOL=OFF',
            '-DDOLFIN_ENABLE_PETSC:BOOL={0}'.format(self.cmake_is_on('petsc')),
            '-DDOLFIN_ENABLE_PETSC4PY:BOOL={0}'.format(self.cmake_is_on('py-petsc4py')),
            '-DDOLFIN_ENABLE_PYTHON:BOOL={0}'.format(self.cmake_is_on('python')),
            '-DDOLFIN_ENABLE_SCOTCH:BOOL={0}'.format(self.cmake_is_on('scotch')),
            '-DDOLFIN_ENABLE_SLEPC:BOOL={0}'.format(self.cmake_is_on('slepc')),
            '-DDOLFIN_ENABLE_SLEPC4PY:BOOL={0}'.format(self.cmake_is_on('py-slepc4py')),
            '-DDOLFIN_ENABLE_SPHINX:BOOL={0}'.format(self.cmake_is_on('py-sphinx')),
            '-DDOLFIN_ENABLE_TRILINOS:BOOL={0}'.format(self.cmake_is_on('trilinos')),
            '-DDOLFIN_ENABLE_UMFPACK:BOOL={0}'.format(self.cmake_is_on('suite-sparse')),
            '-DDOLFIN_ENABLE_VTK:BOOL={0}'.format(self.cmake_is_on('vtk')),
            '-DDOLFIN_ENABLE_ZLIB:BOOL={0}'.format(self.cmake_is_on('zlib'))
        ]
        cmake_args.extend(std_cmake_args)
        with working_dir('build', create=True):
            cmake('..', *cmake_args)
            make()
            make('install')

        cmake_args = [
            '-DCMAKE_BUILD_TYPE:STRING={0}'.format('Debug' if '+debug' in spec else 'Release'),
            '-DBUILD_SHARED_LIBS:BOOL={0}'.format(self.cmake_is_on('+shared')),
            '-DCMAKE_PREFIX_PATH:PATH={0}'.format(prefix),
            '-DPYTHON_EXECUTABLE:FILEPATH={0}/python'.format(spec['python'].prefix.bin),
        ]
        cmake_args.extend(std_cmake_args)
        with working_dir('mshr/build', create=True):
            cmake('..', *cmake_args)
            make()
            make('install')
