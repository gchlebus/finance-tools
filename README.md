# finance-tools
[![Build Status](https://travis-ci.com/gchlebus/finance-tools.svg?branch=master)](https://travis-ci.com/gchlebus/finance-tools)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Collection of scripts to help you analyse your investments.

## to\_fixed\_deposit
```
usage: to_fix_deposit.py [-h] [--interest-tax INTEREST_TAX]
                         [--lower-rate LOWER_RATE] [--upper-rate UPPER_RATE]
                         [--rate-step RATE_STEP]
                         input

Check which kind of a fixed deposit with a monthly interest payout would give
the same results as your investment.

positional arguments:
  input                 Input file. First line - list of comma separated
                        monthly payments. Second line - investment value.

optional arguments:
  -h, --help            show this help message and exit
  --interest-tax INTEREST_TAX
                        Tax deduced from paid interests (19%)
  --lower-rate LOWER_RATE
                        Lower interest rate bound (default 0%)
  --upper-rate UPPER_RATE
                        Upper interest rate bound (default 500%)
  --rate-step RATE_STEP
                        Interest rate step used in search (default 0.05%)
```
