# -*- coding: utf-8 -*-

"""17. Difference in character string in the first column"""

import os
import sys
import subprocess
from collections import OrderedDict


class differenceCharacter:
    """differenceCharacter"""

    def __init__(self, filepath, tmppath):
        self.initialize()
        input_data = self.readFile(filepath)
        input_set = self.setOrderJoin(self.firstString(input_data))
        self.correctCheck(input_set, filepath, tmppath)
        self.cleanTmpFiles(tmppath)

    def initialize(self):
        os.chdir(os.path.dirname(sys.argv[0]))

    def readFile(self, filepath, separator="\n"):
        f = open(filepath)
        return f.read().split(separator)

    def writeFile(self, filepath, values):
        f = open(filepath, "w")
        f.write("\n".join(values))

    def runSubprocess(self, cmd, get_result=True):
        sp = subprocess.run(cmd, stdout=subprocess.PIPE)
        if (get_result):
            return sp.stdout.decode("utf-8")
        return sp

    def firstString(self, listdata, type="tuple"):
        if type == "tuple":
            return [
                (x.split("\t")[0], x.split("\t")[0])
                for x
                in listdata
                if x.split("\t")[0]
            ]
        else:
            return [
                x.split("\t")[0]
                for x
                in listdata
                if x.split("\t")[0]
            ]

    def setOrderJoin(self, listdata):
        return "\n".join(OrderedDict(sorted(listdata))) + "\n"

    def correctCheck(self, input_set, filepath, tmppath):
        tmppath = os.path.realpath(tmppath)
        check_data = self.firstString(self.readFile(filepath), "single")
        self.writeFile(tmppath, check_data)
        self.runSubprocess(["sort", "-o", tmppath, tmppath], False)
        check_set = self.runSubprocess(["uniq", tmppath], True)
        print(input_set)
        print(check_set)
        print(check_set == input_set)

    def cleanTmpFiles(self, tmppath):
        realpath = os.path.realpath(tmppath)
        if os.path.isfile(realpath):
            os.unlink(realpath)


differenceCharacter("data/hightemp.txt", "data/tmp17.txt")
