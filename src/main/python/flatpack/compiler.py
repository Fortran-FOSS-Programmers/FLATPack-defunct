#!/usr/bin/env python
"""
compiler.py, module definition of Compiler class. This class represents
a locally installed compiler of a particular version. These would be
generated when update is run then stored, pickled, in files. They would
be loaded when install or compile are run. This module would also
contain a dictionary mapping compiler names and versions to the
corresponding object.
"""

class Compiler(object):
    
    def __init__(self,command):
        self._command = command
        self._vendor  = ''
        self._version = ''
    
    @property
    def command(self):
        return self._command
    
    @property
    def vendor(self):
        return self._vendor
    
    @property
    def version(self):
        return self._version
    
    
