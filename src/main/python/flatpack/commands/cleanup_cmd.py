#!/usr/bin/env python
"""
cleanup.py, module definition of cleanup command. Removes any packages
installed as dependencies which are no longer needed.
"""

import click

@click.command()
def cleanup_run():
    pass
