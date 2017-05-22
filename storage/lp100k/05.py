# -*- coding: utf-8 -*-

"""05. N-gram."""


def strNgram(x, n):
    """Get N-gram to str."""
    words = x.split()
    enumerate_words = enumerate(words)
    return [
        words[i:i + n]
        for i, y
        in enumerate_words
        if i + n - 1 < len(words)
    ]


def strBigram(x):
    """Get Bi-gram to str."""
    return strNgram(x, 2)


def strTrigram(x):
    """Get Tri-gram to str."""
    return strNgram(x, 3)


print(strBigram("I am an NLPer"))
