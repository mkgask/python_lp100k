# -*- coding: utf-8 -*-

"""19. Arrange character strings in the 1st column in descending order of appearance frequency"""

import os
import sys
import subprocess
from collections import OrderedDict


class ApperanceFrequency:
    """ApperanceFrequency"""

    sp = []

    def __init__(self, file_path, freq_column):
        self.initialize()

        # ファイル読み込み
        read_data = self.readFile(file_path)
        print('readFile: ' + str(read_data))

        read_data = self.selectColumn(read_data, freq_column)
        print('selectColumn: ' + str(read_data))

        count_data = self.freqAppearance(read_data)
        print('freqAppearance: ' + str(count_data))

        count_data = self.reverseSort(count_data, lambda x: x[1])
        print('reverseSort: ' + str(count_data))

        result_data = self.clearOutput(count_data)
        print('clearOutput: ' + str(result_data))

        cmd_column = str(freq_column + 1)
        command = '''
            cut -f{cmd_column} {file_path} | sort | uniq -c | sort -r
        '''.format(cmd_column=cmd_column, file_path=file_path).strip()

        command_result = self.runSubProcess(command, True)
        print('command_result: ' + str(command_result))

        print(result_data == command_result)

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

    def selectColumn(self, read_data, column_number):
        return [
            x.split()[column_number]
            for x
            in read_data
        ]

    def freqAppearance(self, read_data):
        return OrderedDict([
            [x, read_data.count(x)]
            for x
            in read_data
        ])

    def reverseSort(self, sort_data, key_lambda):
        return sorted(sort_data.items(), key=key_lambda, reverse=True)
        # sort_data.sort(key=key_lambda, reverse=True)

    def clearOutput(self, count_data):
        return "\n".join([
            " ".join([str(x[1]), x[0]])
            for x
            in count_data
        ])

    def runSubProcess(self, command, get_result=True):
        self.sp = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        if get_result:
            return self.sp.stdout.decode('utf-8')
        return None


ApperanceFrequency("data/hightemp.txt", 0)  # start is zero from list
