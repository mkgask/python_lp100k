# -*- coding: utf-8 -*-

"""23. Section structure"""

import os
import sys
import gzip
import json
import re


class ReadJson:
    """Read JSON file"""

    readfiles = {}

    def __init__(self):
        self.initialize()

    def load(self, file_path, search_keyword):
        read_data = self.loadFile(file_path)
        json_data = self.decodeJsonMulti(read_data)

        r = []
        for json_one in json_data:
            if (search_keyword in json_one['title']) or \
                    (search_keyword in json_one['text']):
                r.append(json_one['text'])
        return r

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


class SectionStructure:
    """SectionStructure"""

    def __init__(self):
        return

    def pick(self, json_data):
        re_m = re.compile('^=+[^=]+=+$')
        re_section = re.compile('^=+([^=]+)=+$')
        result = []
        for json_one in json_data:
            for one_line in json_one.split():
                r = re_m.findall(one_line)
                if r:
                    result.append((
                        re_section.match(r[0])[0],
                        (r[0].count('=') / 2) - 1
                    ))
        return result


json_data = ReadJson().load('data/jawiki-country.json.gz', 'イギリス')
for output in SectionStructure().pick(json_data):
    print(output)
