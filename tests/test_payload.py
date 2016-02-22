from __future__ import absolute_import, division, print_function       # , unicode_literals
import sys,os
from ..basespaceapp.payload import payload


def test_payload():

    # TODO resolve issue of needing /data/scratch : OSError: [Errno 2] No such file or directory: '/data/scratch/'

    pass
    # assert(
    #   payload({'param1': 'a', 'param2': 'b','param3': 'c','param4': 'd'}, './')
    #   ==
    # 'param1: ' + 'a' + '\n param2: ' + 'b' + '\n param3: ' + 'c' + '\n param4: ' + 'd'
    # )
