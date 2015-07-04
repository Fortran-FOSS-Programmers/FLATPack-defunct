from pybuilder.core import use_plugin, init, task, Author
from codecs import open
import re

try:
    import pandoc
    import subprocess
    pandoc.core.PANDOC_PATH = subprocess.Popen(["which pandoc"],shell=True,stdout=subprocess.PIPE).communicate()[0][:-1]
    doc = pandoc.Document()
    doc.markdown = open('README.md').read()
    long_description = doc.rst
except:
    long_description = open('README.md').read()

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

__source__ = open('src/main/python/flatpack/__init__.py').read()

authors = [Author(re.search(r'^__author__\s*=\s*"(.*)"', __source__, re.M).group(1),
                  re.search(r'^__email__\s*=\s*"(.*)"', __source__, re.M).group(1))]
version = re.search(r'^__version__\s*=\s*"(.*)"', __source__, re.M).group(1)
license = re.search(r'^__license__\s*=\s*"(.*)"', __source__, re.M).group(1)
description = re.search(r'^__description__\s*=\s*"(.*)"', __source__, re.M).group(1)
url = re.search(r'^__url__\s*=\s*"(.*)"', __source__, re.M).group(1)
name = re.search(r'^__appname__\s*=\s*"(.*)"', __source__, re.M).group(1)

default_task = "publish"


@init
def set_properties(project):
    project.summary = description
    project.description = long_description
    
    project.build_depends_on('coverage')
    project.build_depends_on('flake8')
    project.build_depends_on('frosted')
    project.build_depends_on('pylint')
    project.build_depends_on('pylint')
    project.build_depends_on('pyandoc')
    
    project.depends_on('click')
    
    project.set_property('distutils_classifiers', [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System',
        'Topic :: System :: Software Distribution',
        'License :: OSI Approved :: ' + license,
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ])
    
    project.set_property('coverage_break_build', False)
    
