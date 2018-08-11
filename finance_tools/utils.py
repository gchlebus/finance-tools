# -*- coding: utf-8 -*-

__author__ = 'gchlebus'

from datetime import timedelta
import calendar

def get_last_day_of_month(month, year):
  return calendar.monthrange(year, month)[1]

def month_year_iter(startdate, enddate):
  '''Enddate included.'''
  ym_start= 12*startdate.year + startdate.month - 1
  ym_end= 12*enddate.year + enddate.month
  for ym in range(ym_start, ym_end):
    y, m = divmod(ym, 12)
    yield m+1, y

