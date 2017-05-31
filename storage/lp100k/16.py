# -*- coding: utf-8 -*-

"""16. Divide file into N"""

import os
import sys
import subprocess
import glob
import math
import itertools


class divideFile:
    """DivideFile"""

    def __init__(self, filepath, outpath, n):
        self.initialize()
        data = self.readFileDivide(filepath, n)
        print(data)
        self.correctCheck(data, filepath, outpath)
        self.cleanTmpFiles(outpath)

    def initialize(self):
        os.chdir(os.path.dirname(sys.argv[0]))

    def readFileDivide(self, filepath, n):
        f = open(filepath)
        filedata = f.read().split("\n")
        datalen = len(filedata)
        self.row = math.ceil(datalen / int(n))
        return itertools.zip_longest(*[iter(filedata)]*(self.row-1))

    def readFile(self, filepath):
        f = open(filepath)
        return f.read()

    def correctCheck(self, data, filepath, outpath):
        subprocess.run(["split", "--lines=" + str(self.row-1), filepath, outpath], stdout=subprocess.PIPE)
        filelist = glob.glob(outpath + "*")
        for filename, dataOne in zip(filelist, data):
            dataOne = "\n".join(dataOne) + "\n"
            realpath = os.path.realpath(filename)
            filedata = self.readFile(realpath)
            print(filedata)
            print(dataOne)
            print(dataOne == filedata)

    def cleanTmpFiles(self, outpath):
        filelist = glob.glob(outpath + "*")
        for filename in filelist:
            realpath = os.path.realpath(filename)
            if os.path.isfile(realpath):
                os.unlink(realpath)


divideFile("data/hightemp.txt", "data/x", sys.argv[1])
