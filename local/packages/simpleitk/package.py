# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os
from spack import *


class Simpleitk(PythonPackage):
    """
    SimpleITK is a cross-language programming interface to the open-source 
    Insight Toolkit (ITK), whose primary goal is to provide a high level of usability. 
    SimpleITK facilitates rapid prototyping and use of ITK's algorithms from an interactive interpreter. 
    """

    homepage = "http://www.simpleitk.org"
    url      = "http://www.simpleitk.org"
    git      = "https://github.com/SimpleITK/SimpleITKPythonPackage.git"

    version('1.2.0', tag='v1.2.0', submodules=True)

    depends_on('py-numpy')
    depends_on('py-scikit-build', type='build')
    depends_on('cmake', type='build')
    depends_on('ninja', type='build')
    #depends_on('swig', type='build')
    #depends_on('itk')

                                                                        
