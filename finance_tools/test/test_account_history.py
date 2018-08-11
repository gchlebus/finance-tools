# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

from ..account_history import AccountHistory

from datetime import date

FILEPATH = 'finance_tools/test/data/account_history.csv'

def test_len():
  a = AccountHistory(FILEPATH, 2)
  assert len(a) == 3

def test_column_names():
  a = AccountHistory(FILEPATH, 2)
  assert a.columns() == ['Data', 'Amount']

def test_get_rows():
  a = AccountHistory(FILEPATH, 2)
  assert len(a.rows()) == 3
  assert len(a.rows(Data='A')) == 2
  assert len(a.rows(Data=('A', 'B'))) == 3
  rows = a.rows(Amount=-200)
  assert len(rows) == 1
  assert rows.iloc[0]['Amount'] == -200

def test_get_rows_inplace():
  a = AccountHistory(FILEPATH, 2)
  a.rows(Data='A', inplace=True)
  assert len(a) == 2

def test_sum():
  a = AccountHistory(FILEPATH, 2)
  assert a.sum() == 800

def test_date_sorting():
  a = AccountHistory(FILEPATH, 2)
  assert a.rows().iloc[0]['Amount'] == -300

def test_startdate():
  a = AccountHistory(FILEPATH, 2)
  assert a.startdate() == date(2018, 02, 02)

def test_enddate():
  a = AccountHistory(FILEPATH, 2)
  assert a.enddate() == date(2018, 06, 05)
  
def test_get_monthly_amounts():
  a = AccountHistory(FILEPATH, 2)
  v = a.get_monthly_amounts(date(2018, 06, 05))
  assert len(v) == 5
  assert v == [300, 0, 0, 200, 300]

  v = a.get_monthly_amounts(date(2018, 06, 04))
  assert len(v) == 5
  assert v == [300, 0, 0, 200, 0]

  v = a.get_monthly_amounts(date(2018, 07, 04))
  assert len(v) == 6
  assert v == [300, 0, 0, 200, 300, 0]

