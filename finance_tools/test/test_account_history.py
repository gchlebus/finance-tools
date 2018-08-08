# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

from ..account_history import AccountHistory

FILEPATH = 'finance_tools/test/data/account_history.csv'

def test_column_names():
  a = AccountHistory(FILEPATH, 2)
  assert a.columns() == ['Date', 'Data', 'Amount']

def test_get_rows():
  a = AccountHistory(FILEPATH, 2)
  assert len(a.rows()) == 3
  assert len(a.rows(Data='A')) == 2
  assert len(a.rows(Data=('A', 'B'))) == 3
  rows = a.rows(Amount=-200)
  assert len(rows) == 1
  assert rows.iloc[0]['Amount'] == -200

