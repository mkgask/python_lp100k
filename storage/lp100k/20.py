# -*- coding: utf-8 -*-

"""20. Read JSON file"""

import os
import sys
import gzip
import json


class ReadJson:
    """Read JSON file"""

    readfiles = {}

    def __init__(self, file_path, search_keyword):
        self.initialize()

        read_data = self.loadFile(file_path)
        # print('loadFile: ' + str(read_data[0]))

        json_data = self.decodeJsonMulti(read_data)
        print('json_data: ' + str(json_data[0].keys()))
        # print('json_data: ' + str(type(json_data[0])))
        # print('json_data[0][title]: ' + str(json_data[0]['title']))

        for json_one in json_data:
            if (search_keyword in json_one['title']) or \
                    (search_keyword in json_one['text']):
                print(json_one['text'])

    def initialize(self):
        os.chdir(os.path.dirname(sys.argv[0]))

    def loadFile(self, file_path, enc='utf-8'):
        if file_path[-3::] == '.gz':
            with gzip.open(file_path) as f:
                return f.read().decode(enc).splitlines()
        else:
            with open(file_path) as f:
                return f.read().decode(enc).splitlines()
        return []

    def decodeJsonMulti(self, json_data):
        return [
            json.loads(x)
            for x
            in json_data
        ]

    def decodeJsonSingle(self, json_data):
        return json.loads(json_data).split()

    def saveFile(self, file_path, file_data):
        with open(file_path, 'w') as f:
            f.write(file_data)


ReadJson('data/jawiki-country.json.gz', 'イギリス')
