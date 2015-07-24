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

import yaml

class Compiler(yaml.YAMLObject):
    yaml_tag = '!Compiler'
    def __init__(self,vendor,version,command,activate):
        self.vendor = vendor
        self.version = version
        self.command = command
        self.activate = activate    
    
    def __repr__(self):
        return "{}(vendor='{}', version='{}', command='{}', "\
            "activate='{}')".format(self.__class__.__name__, self.vendor,
                                  self.version, self.command,
                                  self.activate)

    def load(self):
        """
        Load the compiler into the path (for example, using GNU
        Modules).
        """
        if self.activate:
            print('Not yet implemented')
            exit
        pass

if __name__ == '__main__':
    import yaml
    src = open('../../../../compilers.yml','r')
    test = yaml.load(src)
    print test
    
