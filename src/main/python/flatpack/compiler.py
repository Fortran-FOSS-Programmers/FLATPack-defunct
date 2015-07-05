#!/usr/bin/env python
"""
compiler.py, module definition of Compiler class. This class represents
a locally installed compiler of a particular version. These would be
generated when update is run then stored, pickled, in files. They would
be loaded when install or compile are run. This module would also
contain a dictionary mapping compiler names and versions to the
corresponding object.
"""

# Vendor IDs
ABSOFT = 1
CRAY = 2
G95 = 3
GNU = 4
HP = 5
IBM = 6
INTEL = 7
NAG = 8
ORACLE = 9
PATHSCALE = 10
PGI = 11

class Compiler(object):
    
    def __init__(self,vendor,version,command,activate):
        self._vendor = vendor
        self._version = version
        self._command = command
        self._activate = activate
    
    def load(self):
        """
        Load the compiler into the path (for example, using GNU
        Modules).
        """
        if self._activate:
            print('Not yet implemented')
            exit
        pass
    
    @property
    def command(self):
        return self._command
    
    @property
    def vendor(self):
        return self._vendor
    
    @property
    def version(self):
        return self._version
    
    
