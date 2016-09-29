#bubblesort

inputdata = """
23
9 2 12 16 22 19 18 7 6 8 20 4 5 1 10 17 13 14 15 21 3 11 23
"""

inlist = [int(x) for x in inputdata.split()]
arraylen = inlist.pop(0)
swapnum = 0
passnum = 0
swapped = True
while swapped:
    swapped = False
    for x in range(arraylen - 1):
        if inlist[x] > inlist[x + 1]:
            inlist[x], inlist[x + 1] = inlist[x + 1], inlist[x]
            swapnum += 1
            swapped = True
    passnum += 1

print inlist
print "%d %d" % (passnum, swapnum)
