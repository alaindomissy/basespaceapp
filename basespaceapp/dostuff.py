########################################################################################################################
#
# DOSTUFF
#
# API functions: dostuff
#
########################################################################################################################

from __future__ import absolute_import, division, print_function    # , from __future__ import unicode_literals


def dostuff(param1, param2, param3, param4, filepath):
    result = 'param1: ' + param1 + '\nparam2: ' + param2 + '\nparam3: ' + param3 + '\nparam4: ' + param4
    with open(filepath, 'w') as filehandle:
        filehandle.write(result)
    return result
