# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

import click
from finance_tools.fix_deposit import fix_deposit
from account_history import AccountHistory

@click.group()
@click.argument('input', type=click.File())
@click.option('--header-row', '-r', type=click.INT, default=2, show_default=True)
@click.option('--date-colname', type=click.STRING, default='Date', show_default=True)
@click.pass_context
def cli(ctx, input, header_row, date_colname):
  ''' Read account history csv file from INPUT and perform a COMMAND.
  '''
  ctx.obj = AccountHistory(input, header=header_row, date_colname=date_colname)

cli.add_command(fix_deposit)

if __name__ == '__main__':
  cli()

