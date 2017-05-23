# -*- coding: utf-8 -*-

"""06. set"""


def charNgram(x, n):
    """Get N-gram to char."""
    x = x.replace(' ', '')
    return [
        x[i:i + n]
        for i, y
        in enumerate(x)
        if i + n < len(x)
    ]


def charBigram(x):
    """Get Bi-gram to char."""
    return charNgram(x, 2)


x = set(charBigram("paraparaparadise"))
y = set(charBigram("paragraph"))

print(x | y)
print(x & y)
print(x - y)
print("se" in x)
print("se" in y)
