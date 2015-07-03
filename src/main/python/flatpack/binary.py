#!/usr/bin/env python
"""
binary.py, module definition of Binary class. This class represents
a particular installation of a package.
"""

from .compiler import Compiler

class Binary(object):
    
    def __init__(self, package, compiler):
        self._package  = package
        self._version  = ''
        self._compiler = compiler
        self._binaries = [] #
        self._includes = [] # lists of paths
        self._docs     = [] #
    
    def remove(self):
        """
        Remove this particular compiled version of the package from the
        system.
        """
        pass
    
    @property
    def package(self):
        return self._package
    
    @property
    def version(self):
        return self._version
        
    @property
    def compiler(self):
        return self._compiler
    
