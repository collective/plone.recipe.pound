# -*- coding: utf-8 -*-
# Copyright (C)2007 'Ingeniweb'

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING. If not, write to the
# Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
This module contains the tool of plone.recipe.pound
"""

import os
from setuptools import setup, find_packages

version = '0.5.0'

README = os.path.join(os.path.dirname(__file__),
              'plone',
              'recipe',
              'pound', 'docs', 'README.txt')

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('plone', 'recipe', 'pound', 'docs', 'building.txt')
    + '\n' +
    read('plone', 'recipe', 'pound', 'docs' , 'configuring.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )




entry_point = 'plone.recipe.pound:Recipe'

entry_points = {"zc.buildout": ["build = plone.recipe.pound:BuildRecipe",
                                "config = plone.recipe.pound:ConfigureRecipe",]}

tests_require=['zope.testing', 'zc.buildout', 'Cheetah']


setup(name='plone.recipe.pound',
      version=version,
      description="Recipe to install and configure Pound",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='pound zope plone recipe',
      author='Ingeniweb',
      author_email='support@ingeniweb.com',
      url='http://plone.org/products/plone-recipes',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.recipe'],
      include_package_data=True,

      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.buildout',
          # -*- Extra requirements: -*-
          'zc.recipe.cmmi',
          'Cheetah',
      ],
      entry_points=entry_points,
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      )
