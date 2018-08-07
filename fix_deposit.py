# -*- coding: utf-8 -*-

import numpy as np

def fix_deposit(monthly_payments, investment_value, interest_tax=19, lower=0, upper=500,
                   step=0.5):
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

if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='Check which kind of a fixed deposit '
    'with a monthly interest payout would give the same results as '
    'your investment.')
  parser.add_argument('input', type=str, help='Input file. First line - list of comma separated monthly payments. Second line - investment value.')
  parser.add_argument('--interest-tax', type=float, default=19,
                      help='Tax deduced from paid interests (%(default).0f%%)')
  parser.add_argument('--lower-rate', type=float, default=0,
                      help='Lower interest rate bound (default %(default).0f%%)')
  parser.add_argument('--upper-rate', type=float, default=500,
                      help='Upper interest rate bound (default %(default).0f%%)')
  parser.add_argument('--rate-step', type=float, default=0.05,
                      help='Interest rate step used in search (default %(default).2f%%)')

  args = parser.parse_args()
  payments, value = read_file(args.input)
  rate, end_value = to_fix_deposit(payments, value, args.interest_tax, args.lower_rate, args.upper_rate, args.rate_step)
  print('INVESTMENT')
  print('  payments           : %d' % len(payments))
  print('  sum payments       : %.2f' % sum(payments))
  print('  value              : %.2f' % value)
  print('FIXED DEPOSIT WITH MONTHLY INTEREST PAYOUT')
  print(' yearly interest rate: %.2f%%' % rate)
  print(' value               : %.2f' % (end_value))

  
  
