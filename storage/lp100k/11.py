# -*- coding: utf-8 -*-

"""11. Convert tab to space"""

import os
import sys
import subprocess

__dir__ = os.path.dirname(sys.argv[0])


def convertT2S(filepath):
    os.chdir(__dir__)
    r = subprocess.run(["expand", filepath], stdout=subprocess.PIPE)
    return r.stdout.decode('utf-8')  # Adjust output


print(convertT2S("./data/hightemp.txt"))
