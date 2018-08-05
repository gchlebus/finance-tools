# -*- coding: utf-8 -*-
__author__ = 'gchlebus'

from to_fix_deposit import to_fix_deposit

def test_one_mo_rate():
  assert 1.5 == to_fix_deposit([100], 101.5)[0]

def test_two_mos_rate():
  assert 2. == to_fix_deposit([100, 200], 308.04)[0]
  
