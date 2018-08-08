# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

import click
from finance_tools.fix_deposit import fix_deposit

@click.group()
def cli():
  pass

cli.add_command(fix_deposit)

