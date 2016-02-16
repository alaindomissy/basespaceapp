from __future__ import absolute_import, division, print_function
import sys,os
sys.path.insert(0,os.path.abspath(__file__+"/../.."))

from pybasespace.payload import payload


def test_payload():
    assert(
      payload({'param1': 'a', 'param2': 'b','param3': 'c','param4': 'd',}, './')
      ==
    'param1: ' + 'a' + '\n param2: ' + 'b' + '\n param3: ' + 'c' + '\n param4: ' + 'd'
    )
