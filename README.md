# finance-tools
[![Build Status](https://travis-ci.com/gchlebus/finance-tools.svg?branch=master)](https://travis-ci.com/gchlebus/finance-tools)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Collection of scripts to help you analyse your investments.

## Usage
```
Usage: ft [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  fix_deposit  Check what kind of a fixed deposit with a...
```

## ft fixed\_deposit
```
Usage: ft fix_deposit [OPTIONS] INPUT

  Check what kind of a fixed deposit with a monthly interest payout would
  give the same results as your investment.

Options:
  --interest-tax FLOAT  Tax deduced from paid interests  [default: 19.0]
  --help                Show this message and exit.
```

### Example
investment.txt
```
100,100,100,100,100,100,100,100,200,200,200,200,200,200,200,200,200,200,200,200
3482
```
```
/ft fix_deposit investment.txt
INVESTMENT
  payments           : 20
  sum payments       : 3200.00
  value              : 3482.00
FIXED DEPOSIT WITH MONTHLY INTEREST PAYOUT
 yearly interest rate: 13.75%
 value               : 3481.77
```

