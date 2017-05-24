# -*- coding: utf-8 -*-

"""07. Sentence generation by template"""


def template(x, y, z):
    return "%s時の%sは%s" % (x, y, z)


print(template("12", "気温", "22.4"))
