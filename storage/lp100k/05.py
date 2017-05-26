# -*- coding: utf-8 -*-

"""05. N-gram."""


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


def charTrigram(x):
    """Get Bi-gram to char."""
    return charNgram(x, 3)


def wordNgram(x, n):
    """Get N-gram to str."""
    words = x.split()
    enumerate_words = enumerate(words)
    return [
        words[i:i + n]
        for i, y
        in enumerate_words
        if i + n - 1 < len(words)
    ]


def wordBigram(x):
    """Get Bi-gram to str."""
    return wordNgram(x, 2)


def wordTrigram(x):
    """Get Tri-gram to str."""
    return wordNgram(x, 3)


print(wordBigram("I am an NLPer"))
print(charBigram("I am an NLPer"))
