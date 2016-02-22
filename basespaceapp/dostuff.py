########################################################################################################################
#
# DOSTUFF
#
# API functions: dostuff
#
########################################################################################################################

from __future__ import absolute_import, division, print_function    # , unicode_literals


def dostuff(params_value, filepath):

    result = '\n'.join([key + ': ' + value for key, value in params_value])
    # result = 'param1: ' + param1 + '\nparam2: ' + param2 + '\nparam3: ' + param3 + '\nparam4: ' + param4

    with open(filepath, 'w') as filehandle:
        filehandle.write(result)
    return result
