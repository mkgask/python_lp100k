# -*- coding: utf-8 -*-

"""15. Output file tail"""

import os
import sys
import subprocess


class outputFileTail:
    """Output File Tail"""

    result = False

    def __init__(self, filepath, row):
        self.initialize()
        data = self.readFileTail(filepath, row)
        print(data)
        self.result = self.correctCheck(data, filepath, row)

    def initialize(self):
        os.chdir(os.path.dirname(sys.argv[0]))

    def readFileTail(self, filepath, row):
        f = open(filepath)
        filedata = f.read().split("\n")
        return "\n".join(filedata[(int(row) + 1) * -1:])

    def correctCheck(self, data, filepath, row):
        r = subprocess.run(["tail", "-n" + row, filepath], stdout=subprocess.PIPE)
        ret = r.stdout.decode("utf-8")
        print(ret)
        return data == ret


o = outputFileTail("data/hightemp.txt", sys.argv[1])
print(o.result)
