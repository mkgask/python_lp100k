# -*- coding: utf-8 -*-

"""13. Two file merge"""

import os
import sys
import subprocess

# Initialize
__dir__ = os.path.dirname(sys.argv[0])
os.chdir(__dir__)


def readFile(filepath):
    f = open(filepath)
    return f.read()


def correctCheck(data, filepath1, filepath2):
    r = subprocess.run(["paste", filepath1, filepath2], stdout=subprocess.PIPE)
    ret = r.stdout.decode("utf-8")
    print(ret)
    return data == ret


def twoFileMerge(filepath1, filepath2):
    col1 = readFile(filepath1)
    col2 = readFile(filepath2)
    result = "\n".join([
        c1 + "\t" + c2
        for c1, c2
        in zip(col1.split(), col2.split())
    ]) + "\n"
    print(result)
    return correctCheck(result, filepath1, filepath2)


print(twoFileMerge("data/col1.txt", "data/col2.txt"))
