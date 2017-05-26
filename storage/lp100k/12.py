# -*- coding: utf-8 -*-

"""11. Split save"""

import os
import sys
import subprocess

# Initialize
__dir__ = os.path.dirname(sys.argv[0])
os.chdir(__dir__)


def readColumn(filepath):
    pref_list = []
    city_list = []
    for line in open(filepath):
        item_list = line.split("\t")
        pref_list.append(item_list[0] + "\n")
        city_list.append(item_list[1] + "\n")
    return (pref_list, city_list)


def writeFile(filepath, values):
    f = open(filepath, "w")
    f.writelines(values)


def correctCheck(filepath1, column, filepath2, ):
    r = subprocess.run(["cut", "-f" + str(column), filepath1], stdout=subprocess.PIPE)
    data1 = r.stdout.decode("utf-8")  # Adjust output
    data2 = open(filepath2).read()
    print(data1)
    print(data2)
    print(data1 == data2)


def splitSave(filepath):
    item_list = readColumn(filepath)
    writeFile("data/col1.txt", item_list[0])
    writeFile("data/col2.txt", item_list[1])
    correctCheck("data/hightemp.txt", 1, "data/col1.txt")
    correctCheck("data/hightemp.txt", 2, "data/col2.txt")


splitSave("data/hightemp.txt")
