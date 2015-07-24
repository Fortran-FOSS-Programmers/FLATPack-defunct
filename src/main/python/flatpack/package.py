#!/usr/bin/env python
"""
package.py, module definition of Package class. This class represents
individual packages managed by FLATPack.
"""

import yaml

class Package(yaml.YAMLObject):
    """
    Represents a package which can be installed (or removed) by FLATPack.
    """
    yaml_tag = '!Package'
    def __init__(self, json_file, package_list):
        self.name = ''
        self.description = ''
        self.src = ''
        self.versions = {'': '',}
        self.compilers = []
        self.test = ''
        self.dependencies = []
    
    def __repr__(self):
        rep = "{}(name='{}', src='{}',\n"\
              "\tdescription='{}',\n"\
              "\tversions={},\n"\
              "\tcompilers={},\n"\
              "\ttest='{}',\n"\
              "\tdependencies={}\n)"
        return rep.format(self.__class__.__name__, self.name, self.src,
                        self.description, repr(self.versions),
                        repr(self.compilers), self.test,
                        repr(self.dependencies))

    def get_source(self, version):
        """
        Get source for version of package and return CompileEnv object.
        Raise exception if version does not exist.
        """
        pass
    
