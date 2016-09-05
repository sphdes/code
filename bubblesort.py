#bubblesort

inputdata = """
8
3 1 4 1 5 9 2 6
"""

inlist = [int(x) for x in inputdata.split()]
arraylen = inlist.pop(0)
swapnum = 0
passnum = 0
swapcheck = 0
swapj = 1

while swapj != 0:
    for x in range(arraylen - 1):
        if inlist[x] <= inlist[x + 1] not True:
            p = inlist[x]
            inlist[x] = inlist[x + 1]
            inlist[x + 1] = p
            swapnum += 1

    passnum += 1
    swapj = swapcheck - swapnum
    swapcheck = swapnum

print "%d %d" % (swapnum, passnum)
