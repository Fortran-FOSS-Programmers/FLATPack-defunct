#!/usr/bin/env python
"""
local_state.py, module definition of LocalState class.
"""

class LocalState(object):
    """
    This class contains the information about what is currently
    installed locally.
    """
    
    def __init__(self, database, records):
        self._installed_explicit = [] # Lists of Binary objects
        self._installed_depends  = [] #
        
    def __str__(self):
        """
        Returns JSON of self, to be saved to a file.
        """
        pass
    
    def is_installed(self, package_name, package_version):
        """
        Returns true if package already installed, false otherwise.
        """
        return False

    @property
    def installed(self):
        return self._installed_explicit + self._installed_depends
        
    @property
    def installed_explicit(self):
        return self._installed_explicit
        
    @property
    def installed_depends(self):
        return self._installed_depends
    
    
