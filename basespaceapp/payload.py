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
# from .dostuff import dostuff
# from .config import ARGUMENTS_WITH_CONTENT, ARGUMENTS_WITH_ITEMS


def dostuff(params_value, filepath):
    result = '\n'.join([key + ': ' + value for key, value in params_value])
    # result = 'param1: ' + param1 + '\nparam2: ' + param2 + '\nparam3: ' + param3 + '\nparam4: ' + param4
    with open(filepath, 'w') as filehandle:
        filehandle.write(result)
    return result


###################
# MAIN API FUNCTION
###################

def payload(params_value, output_dir, scratch_dir):

    # parse params_value
    ####################
    # param1 = str(params_value['input.param1'])
    # param2 = str(params_value['input.param2'])
    # param3 = str(params_value['input.param3'])
    # param4 = str(params_value['input.param4'])
    # for param in ARGUMENTS_WITH_CONTENT:
    #     pass

    # do stuff with data, saving files into SCRATCH
    ################################################
    result = dostuff(params_value, scratch_dir + 'result.txt')

    # coypy scratch to output_dir, so it is saved as results by basespace
    #####################################################################
    # copytree(source, destination, ignore=_logpath)
    copytree(scratch_dir, output_dir + '../sessiondetails_' + datetime.now().isoformat('_'))

    # return 'param1: ' + 'a' + '\nparam2: ' + 'b' + '\nparam3: ' + 'c' + '\nparam4: ' + 'd'
    return result
