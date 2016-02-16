# sys.path.insert(0, os.path.abspath(__file__+"/../.."))

from __future__ import absolute_import, division, print_function
import sys
import os
from ..basespaceapp.sampleapp import *



def test_main ():

    testdir = os.path.dirname(os.path.abspath(__file__))
    datadir = testdir + '/data/'

    # TODO issue: [Errno 2] No such file or directory: u'/data/output/appresults/27855842/SRR1015697/parameters.csv'
    main(datadir)
