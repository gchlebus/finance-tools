# finance-tools
[![Build Status](https://travis-ci.com/gchlebus/finance-tools.svg?branch=master)](https://travis-ci.com/gchlebus/finance-tools)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Collection of scripts to help you analyse your investments.

## Installation
```
git clone https://github.com/gchlebus/finance-tools.git
cd finance-tools
pip install .
```

## Usage
```
Usage: ft [OPTIONS] INPUT COMMAND [ARGS]...

  Read account history csv file from INPUT and perform a COMMAND.

Options:
  -r, --header-row INTEGER  [default: 2]
  --date-colname TEXT       [default: Date]
  --help                    Show this message and exit.

Commands:
  fix_deposit  Check what kind of a fixed deposit with a...
```

## Commands 

### fix_deposit
```
Usage: ft fix_deposit [OPTIONS] VALUE

  Check what kind of a fixed deposit with a monthly interest payout would
  give the same results as your investment.

Options:
  --interest-tax FLOAT  Tax deduced from paid interests  [default: 19.0]
  -c, --colname TEXT    Column name with amounts.  [default: Amount]
  --help                Show this message and exit.
```

Example
```
ft finance_tools/test/data/account_history.csv fix_deposit 900
INVESTMENT
  payments           : 3
  sum payments       : 800.00
  value              : 900.00
FIXED DEPOSIT WITH MONTHLY INTEREST PAYOUT
 yearly interest rate: 36.90%
 value               : 900.04
```

