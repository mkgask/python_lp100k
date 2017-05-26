# -*- coding: utf-8 -*-

"""10. line count"""

import os
import sys
import subprocess

__dir__ = os.path.dirname(sys.argv[0])
# __dir__ = os.path.dirname(os.path.abspath(__file__)) # maybe late


def lineCount(filepath):
    os.chdir(__dir__)
    r = subprocess.run(["wc", filepath], stdout=subprocess.PIPE)
    return r.stdout.split()[0]


print(lineCount("data/hightemp.txt"))
