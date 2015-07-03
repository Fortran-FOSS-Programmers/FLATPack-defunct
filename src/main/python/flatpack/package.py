#!/usr/bin/env python
"""
package.py, module definition of Package class. This class represents
individual packages managed by FLATPack.
"""

class Package(object):
    """
    Represents a package which can be installed (or removed) by FLATPack.
    """
    
    def __init__(self, json_file):
        self._data_file = json_file
        
    
