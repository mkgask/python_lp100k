# -*- coding: utf-8 -*-

"""08. Cipher Text"""


def cipher(text):
    return ''.join([
        chr(219 - ord(char)) if char.islower() else char
        for char
        in text
    ])


print("I am an NLPer : " + cipher("I am an NLPer"))
