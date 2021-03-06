#!/usr/bin/env python
"""
FLATPack, Fortran Library, Application, and Tool Packaging

Main program driver. Parses CLI and calls appropriate methods to run
the program.
"""
__appname__     = "FLATPack"
__description__ = "FLATPack, Fortran Library, Application, and Tool Packaging"
__version__     = "0.0.1"
__author__      = "Chris MacMackin"
__email__       = "cmacmackin@gmail.com"
__license__     = "GNU General Public License v3 (GPLv3)"
__url__         = "https://github.com/Fortran-FOSS-Programmers/FLATPack"
__maintainer__  = "Chris MacMackin"
__status__      = "Production"

import click
from .commands.cleanup_cmd import cleanup_run
from .commands.compile_cmd import compile_run
from .commands.help_cmd import help_run
from .commands.list_cmd import list_run
from .commands.remove_cmd import remove_run
from .commands.search_cmd import search_run
from .commands.update_cmd import update_run
from .commands.upgrade_cmd import upgrade_run

@click.group()
def main():
    pass
    
main.add_command(cleanup_run, name="cleanup")
main.add_command(compile_run, name="compile")
main.add_command(help_run, name="help")
main.add_command(list_run, name="list")
main.add_command(remove_run, name="remove")
main.add_command(search_run, name="search")
main.add_command(update_run, name="update")
main.add_command(upgrade_run, name="upgrade")
