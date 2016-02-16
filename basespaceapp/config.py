########################################################################################################################
#
# CONFIG
#
# API functions:
#
########################################################################################################################

from __future__ import absolute_import, division, print_function
# from __future__ import unicode_literals
import os

from shutil import rmtree
from subprocess import check_output

SCRATCH = os.environ.get('SCRATCH','/data/scratch/')
# SCRATCH = './'

APPSESS = os.environ.get('APPSESS', '/data/input/AppSession.json')
