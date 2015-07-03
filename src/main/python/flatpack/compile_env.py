#!/usr/bin/env python
"""
compile_env.py, module definition of CompileEnv class. This class 
represents the directory in which compilation is to be performed. It
contains information on how to compile and methods to perform the
compilation.
"""

class CompileEnv(object):
    
    def __init__(self, location, package, version=None):
        self._location = ''
        self._package = package
        # Get various information about the build process

    def compile(self, compiler):
        """
        Compile the package, using the specified compiler, if possible.
        If compilation succesful then will return an Installer object.
        Otherwise raises exceptions.
        """
        pass
        
    def remove(self):
        """
        Remove the directories containing the compilation environment.
        """
        # This might be better structured as a destructor
        pass
