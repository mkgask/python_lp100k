# -*- coding: utf-8 -*-

"""09. Cipher Typoglycemia"""


import random


def typoglycemia(text):
    return " ".join([
        word if len(word) <= 4 else word[0] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
        for word
        in text.split()
    ])


print(typoglycemia("I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
