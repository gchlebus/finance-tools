# -*- coding: utf-8 -*-

import pandas as pd

class AccountHistory(object):
  def __init__(self, filename, header=0):
    self._df = pd.read_csv(filename, header=header)

  def columns(self):
    return self._df.columns.tolist()

  def rows(self, **kwargs):
    ret = self._df
    for key, value in kwargs.items():
      if not isinstance(value, (list, tuple)):
        value = [value]
      ret = pd.concat([ret.loc[ret[key] == v] for v in value])
    return ret
