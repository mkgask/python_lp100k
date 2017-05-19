import re

print([
    len(re.sub('[^a-zA-Z]+', '', x))
    for x
    in "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".split()
])
