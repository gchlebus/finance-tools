# -*- coding: utf-8 -*-
__author__ = 'gchlebus'

from ..fix_deposit import _fix_deposit

def test_one_mo_rate():
  assert 1.5 == _fix_deposit([100], 100.10125)[0]

def test_two_mos_rate():
  assert 2. == _fix_deposit([100, 200], 300.54)[0]
  
