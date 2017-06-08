# -*- coding: utf-8 -*-

"""18. Sort each row by descending order of column 3"""

import os
import sys
import subprocess


class SortByColumn:
    """SortByColumn"""

    def __init__(self, file_path, sort_column):
        self.initialize()

        read_data = self.readFile(file_path)
        read_data = self.sortColumn([x.split() for x in read_data], sort_column)
        read_data = "\n".join(["\t".join(x) for x in read_data]) + "\n"

        cmd_data = self.runSubProcess(["sort", "-t\t", "-rnk" + str(sort_column) + "," + str(sort_column), file_path])

        print(read_data)
        print(cmd_data)
        print(read_data == cmd_data)

    def initialize(self):
        os.chdir(os.path.dirname(sys.argv[0]))
        self.readfiles = {}

    def readFile(self, read_file, use_cache=True, t="r", separator="\n"):
        if use_cache:
            if read_file in self.readfiles:
                return self.readfiles[read_file]
        f = open(read_file, t)
        read_data = [x for x in f.read().split(separator) if x]
        if use_cache:
            self.readfiles[read_file] = read_data
        return read_data

    def sortColumn(self, data, sort_column):
        sorted(data, key=lambda x: x[sort_column])
        return data

    def runSubProcess(self, command, get_result=True):
        sp = subprocess.run(command, stdout=subprocess.PIPE)
        if get_result:
            return sp.stdout.decode('utf-8')
        return None


SortByColumn("data/hightemp.txt", 2)  # start is zero from list
