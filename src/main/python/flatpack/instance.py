#!/usr/bin/env python
"""
instance.py, module definition of Instance class. This class describes
where this instance of FLATPack is to do the compiling and to install
the results, as well as what the state of the system is.
"""

class Instance(object):
    def __init__(self,config):
        self._compile_dir = ''
        self._binary_dir  = ''
        self._header_dir  = ''
        self._doc_dir     = ''
        self._compilers   = [] # List of Compiler objects
        self._local       = LocalState()
        self._packages    = PackageTree()

    def get_binary_path(self,comp_env):
        '''
        Return appropriate path for binaries of whatever is being
        compiled.
        '''
        return ''
    
    def get_header_path(self,comp_env):
        '''
        Return appropriate path for headers/.mod files of whatever is 
        being compiled.
        '''
        return ''
    
    def get_doc_path(self,comp_env):
        '''
        Return appropriate path for documentation of whatever is being
        compiled.
        '''
        return ''
    
    @property
    def compile_dir(self):
        return self._compile_dir
    
