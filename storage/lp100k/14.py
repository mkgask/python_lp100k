# -*- coding: utf-8 -*-

"""14. Output file head"""

import os
import sys
import subprocess


class outputFileHead:
    """Output File Head"""

    result = False

    def __init__(self, filepath, row):
        self.initialize()
        data = self.readFileHead(filepath, row)
        print(data)
        self.result = self.correctCheck(data, filepath, row)

    def initialize(self):
        os.chdir(os.path.dirname(sys.argv[0]))

    def readFileHead(self, filepath, row):
        f = open(filepath)
        filedata = f.read().split("\n")
        return "\n".join(filedata[0:int(row)]) + "\n"

    def correctCheck(self, data, filepath, row):
        r = subprocess.run(["head", "-n" + row, filepath], stdout=subprocess.PIPE)
        ret = r.stdout.decode("utf-8")
        print(ret)
        return data == ret


o = outputFileHead("data/hightemp.txt", sys.argv[1])
print(o.result)
