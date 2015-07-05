#!/usr/bin/env python
"""
package.py, module definition of Package class. This class represents
individual packages managed by FLATPack.
"""

class Package(object):
    """
    Represents a package which can be installed (or removed) by FLATPack.
    """
    
    def __init__(self, json_file, package_list):
        self._data_file = json_file
        self._name = ''
        self._author = ''
        self._description = ''
        self._versions = ['',]
        self._git_repo = ''
        self._version_commits = { '' : '', }
        
    def get_source(self, version):
        """
        Get source for version of package and return CompileEnv object.
        Raise exception if version does not exist.
        """
        pass
        
