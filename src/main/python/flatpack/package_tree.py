#!/usr/bin/env python
"""
package.py, module definition of PackageTree class. This class
represents all packages in the database and their dependencies on each
other.
"""

class PackageTree(object):
    def __init__(self,database):
        self._package_list = []
        
    def __iter__(self):
        return self._package_list
    
    def get_package(self,package_name):
        """
        Looks up the package object in the list and returns it.
        """
        return None
