# sys.path.insert(0, os.path.abspath(__file__+"/../.."))

from __future__ import absolute_import, division, print_function
import sys
import os
from ..basespaceapp.sampleapp import *



def test_metadatajson():

    testdir = os.path.dirname(os.path.abspath(__file__))

    appsession_location = testdir + '/AppSession.json'

    main(appsession_location)
