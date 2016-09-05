#collatzsequence

inputdata = """
2 15 97
"""

inputlist = [int(x) for x in inputdata.split()]

for x in inputlist:
    counter = 0
    while x != 1:
        if (x % 2) == 0:
            x = x / 2
        else:
            x = x * 3 + 1
        counter += 1

    print counter,
