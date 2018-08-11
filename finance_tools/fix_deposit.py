# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

import click
import numpy as np
from account_history import AccountHistory

pass_account_history = click.make_pass_decorator(AccountHistory)

@click.command()
@pass_account_history
@click.argument('value', type=click.FLOAT)
@click.option('--interest-tax', default=19.0, show_default=True, type=click.FLOAT,
              help='Tax deduced from paid interests')
@click.option('--colname', '-c', default='Amount', show_default=True, type=click.STRING,
              help='Column name with amounts.')
def fix_deposit(account_history, value, interest_tax, colname):
  """
  Check what kind of a fixed deposit with a monthly interest payout would
  give the same results as your investment.
  """
  rate, end_value = _fix_deposit(account_history, value, interest_tax, colname=colname)
  print('INVESTMENT')
  print('  payments           : %d' % len(account_history))
  print('  sum payments       : %.2f' % account_history.sum())
  print('  value              : %.2f' % value)
  print('FIXED DEPOSIT WITH MONTHLY INTEREST PAYOUT')
  print(' yearly interest rate: %.2f%%' % rate)
  print(' value               : %.2f' % (end_value))

def _fix_deposit(account_history, investment_value, interest_tax=19, lower=0, upper=500,
                   step=0.05, enddate=None, colname='Amount'):
  '''Computes interest rate of a fixed deposit with a monthly interest payout
  given investment history.
  :param account_history: Account history object.
  :param investment_value: Final investment value.
  '''
  payments = account_history.get_monthly_amounts(enddate, colname=colname)
  months = len(payments)
  def eval(rate):
    real_rate = rate * (1/12.) * (1/100.) * (1-interest_tax/100.)
    return sum([p*(1+real_rate)**(months-idx) for idx, p in enumerate(payments)])

  rates = np.arange(lower, upper, step)
  values = np.asarray(list(map(eval, rates)))
  idx = np.abs(values - investment_value).argmin()
  return rates[idx], values[idx]

