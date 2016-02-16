# sys.path.insert(0, os.path.abspath(__file__+"/../.."))

from __future__ import absolute_import, division, print_function
import sys
import os
from ..basespaceapp.sampleapp import *


def test_json_depcopy():

    assert(json_deepcopy(metadatatemplate) == json_deepcopy(metadatatemplate))

    assert(json_deepcopy(metadatatemplate) is not json_deepcopy(metadatatemplate))


def test_parse_appsessionparams():

    # testdir = os.path.dirname(os.path.abspath(__file__))
    #
    # appsession_location = testdir + '/AppSession.json'
    #
    # appsessionhref1, appsessionparams1 = read_appsession(appsession_location)
    #
    # assert(appsessionhref1 == u'v1pre3/appsessions/31951397')
    #
    # assert(expected)

    pass
