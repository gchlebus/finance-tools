# -*- coding: utf-8 -*-
__author__ = 'gchlebus'

from ..fix_deposit import _fix_deposit
from ..account_history import AccountHistory
import os

TEST_DIR = 'finance_tools/test/data'

def test_one_mo_rate():
  a = AccountHistory(os.path.join(TEST_DIR, 'one_mo_rate.csv'))
  assert 1.5 == _fix_deposit(a, 100.10125, enddate=a.enddate())[0]

def test_two_mos_rate():
  a = AccountHistory(os.path.join(TEST_DIR, 'two_mos_rate.csv'))
  assert 2. == _fix_deposit(a, 300.54, enddate=a.enddate())[0]
  
