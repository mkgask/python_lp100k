from collections import OrderedDict

print(OrderedDict([
    (i, x[0]) if i in [1, 5, 6, 7, 8, 9, 15, 16, 19] else (i, x[0:2])
    for x, i
    in zip(
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split(' '),
        range(1, 21)
    )
]))
