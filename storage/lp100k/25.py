# -*- coding: utf-8 -*-

"""25. Pickup templates"""

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
        return list(map(
            json.loads,
            json_data
        ))

    def decodeJsonSingle(self, json_data):
        return json.loads(json_data).split()

    def saveFile(self, file_path, file_data):
        with open(file_path, 'w') as f:
            f.write(file_data)


class PickupTemplates:
    """PickupTemplates"""

    def __init__(self):
        return

    def pick(self, json_data):
        re_m = re.compile('\{\{基礎情報[^\}]+\}\}')
        # replace_m = re.compile('\|.*$')
        result = []
        for json_one in json_data:
            r = re_m.findall(json_one)
            if r:
                result.append(r)
            """
            for one_line in json_one.split("\n"):
                r = re_m.findall(json_one)
                if r:
                    result.append(r)
                    result.append([
                        replace_m.sub('', cate)
                        for cate
                        in r
                    ])
            """
        return self.extract(result)

    def extract(self, sentence):
        result = []
        for basestr in sentence:
            for basestr2 in basestr:
                r = {}
                for str in basestr2.split('\n|'):
                    if 0 < str.count('='):
                        pair = str.split('=')
                        r[pair[0].strip()] = pair[1].strip()
                result.append(r)
        return result


json_data = ReadJson().load('data/jawiki-country.json.gz', 'イギリス')
[print(r) for r in PickupTemplates().pick(json_data)]
