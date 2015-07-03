#!/usr/bin/env python
"""
compiler.py, module definition of Compiler class. This class represents
a locally installed compiler of a particular version. These would be
generated when update is run then stored, pickled, in files. They would
be loaded when install or compile are run. This module would also
contain a dictionary mapping compiler names and versions to the
corresponding object.
"""
