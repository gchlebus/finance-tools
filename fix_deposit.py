# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

import click
import numpy as np

@click.command()
@click.argument('input', type=click.Path(exists=True))
@click.option('--interest-tax', default=19.0, show_default=True, help='Tax deduced from paid interests')
def fix_deposit(input, interest_tax):
  """Check what kind of a fixed deposit with a monthly interest payout would give the same results as
  your investment.

  """
  payments, value = read_file(input)
  rate, end_value = _fix_deposit(payments, value, interest_tax)
  print('INVESTMENT')
  print('  payments           : %d' % len(payments))
  print('  sum payments       : %.2f' % sum(payments))
  print('  value              : %.2f' % value)
  print('FIXED DEPOSIT WITH MONTHLY INTEREST PAYOUT')
  print(' yearly interest rate: %.2f%%' % rate)
  print(' value               : %.2f' % (end_value))

def _fix_deposit(monthly_payments, investment_value, interest_tax=19, lower=0, upper=500,
                   step=0.05):
  '''Computes interest rate of a fixed deposit with a monthly interest payout
  given investment history.
  :param monthly_payments: list of monthly payments.
  :param investment_value: Final investment value.
  '''
  months = len(monthly_payments)
  def eval(rate):
    real_rate = rate * (1/12.) * (1/100.) * (1-interest_tax/100.)
    return sum([p*(1+real_rate)**(months-idx) for idx, p in enumerate(monthly_payments)])

  rates = np.arange(lower, upper, step)
  values = np.asarray(list(map(eval, rates)))
  idx = np.abs(values - investment_value).argmin()
  return rates[idx], values[idx]

def read_file(filename):
  with open(filename, 'r') as f:
    payments = f.readline()
    value = f.readline()
  return list(map(float, payments.split(','))), float(value)

