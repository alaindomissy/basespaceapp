########################################################################################################################
#
# PAYLOAD
#
# API functions: payload
#
########################################################################################################################

from __future__ import absolute_import, division, print_function   # , unicode_literals

from shutil import copytree
from datetime import datetime

# from .config import SCRATCH
from .dostuff import dostuff


###################
# MAIN API FUNCTION
###################

def payload(params_value, output_dir, scratch_dir):

    # parse params_value
    ####################
    param1 = str(params_value['input.param1'])
    param2 = str(params_value['input.param2'])
    param3 = str(params_value['input.param3'])
    param4 = str(params_value['input.param4'])

    # do stuff with data, saving files into SCRATCH
    ################################################

    dostuff(param1, param2, param3, param4, scratch_dir + 'result.txt')

    # coypy sctach to output_dir, so it is saves as results by basespace
    #####################################################################
    # copytree(source, destination, ignore=_logpath)
    copytree(scratch_dir, output_dir + '../sessiondetails_' + datetime.now().isoformat('_'))

    return 'param1: ' + 'a' + '\nparam2: ' + 'b' + '\nparam3: ' + 'c' + '\nparam4: ' + 'd'
