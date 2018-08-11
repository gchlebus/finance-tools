# -*- coding: utf-8 -*-

import pandas as pd
from datetime import timedelta, date
from .utils import month_year_iter, get_last_day_of_month

class AccountHistory(object):
  def __init__(self, filename, header=0, date_colname='Date'):
    self._df = pd.read_csv(filename, header=header)
    self._to_datetime(date_colname)
    self._sort_by_date()

  def __len__(self):
    return len(self._df)
    
  def columns(self):
    return self._df.columns.tolist()

  def rows(self, **kwargs):
    inplace = kwargs.pop('inplace', False)
    ret = self._df
    for key, value in kwargs.items():
      if not isinstance(value, (list, tuple)):
        value = [value]
      ret = pd.concat([ret.loc[ret[key] == v] for v in value])
    if inplace:
      self._df = ret
    return ret

  def sum(self, colname='Amount'):
    return self._df[colname].abs().sum()
  
  def startdate(self):
    return self._df.index[0].to_pydatetime().date()

  def enddate(self):
    return self._df.index[-1].to_pydatetime().date()

  def get_monthly_amounts(self, enddate=None, colname='Amount'):
    if not enddate:
      enddate = date.today()
    amounts = []
    df = self._df[self.startdate():enddate]
    for month, year in month_year_iter(self.startdate(), enddate):
      b = date(year, month, 1)
      e = date(year, month, get_last_day_of_month(month, year))
      amounts.append(df[b:e][colname].abs().sum())
    return amounts
  
  def _to_datetime(self, date_colname):
    format = '%Y-%m-%d'
    self._df[date_colname] = pd.to_datetime(self._df[date_colname], format=format)
    self._df.set_index(date_colname, inplace=True)
    
  def _sort_by_date(self):
    self._df.sort_index(inplace=True)
  
