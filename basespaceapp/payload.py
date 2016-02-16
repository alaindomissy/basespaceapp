########################################################################################################################
#
# PAYLOAD
#
# API functions: payload
#
########################################################################################################################

from __future__ import absolute_import, division, print_function
# from __future__ import unicode_literals

from shutil import copytree
from datetime import datetime

from .config import SCRATCH
from .dostuff import dostuff


###################
# MAIN API FUNCTION
###################

def payload(params_value, output_dir):

    # parse params_value
    ####################
    param1 = str(params_value['param1'])
    param2 = str(params_value['param2'])
    param3 = str(params_value['param3'])

    # do stuff with data, saving files into SCRATCH
    ################################################
    dostuff(param1, param2, param3, SCRATCH)

    # coypy sctach to output_dir, so it is saves as results by basespace
    #####################################################################
    # copytree(source, destination, ignore=_logpath)
    copytree(SCRATCH, output_dir + '../sessiondetails_' + datetime.now().isoformat('_'))

    return
