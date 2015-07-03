#!/usr/bin/env python
"""
installer.py, module definition of Installer class. This class
represents where compiled binaries, .mod file, headers, and
documentation would go for a package. It would contain methods to place
these things in their corresponding locations.
"""

class Installer(object):
    def __init__(self, binaries, headers, docs):
        self._binaries = binaries
        self._headers  = headers
        self._docs     = docs
    
    def install(self,dest):
        """
        Place the binaries, headers, and docs in the appropriate
        locations. Return a Binary object if successful. Otherwise
        raise exceptions.
        """
        pass
        
