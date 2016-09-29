#indexsort

pin = """
20
398 356 658 965 807 138 615 867 716 761 193 248 456 304 87 44 920 1014 516 572
"""
plist = [int(x) for x in pin.split()]
pcase = plist.pop(0)
pdex = range(1, pcase + 1 , 1)
swapped = True
while swapped:
    swapped = False
    for x in range(pcase - 1):
        if plist[x] > plist[x + 1]:
            plist[x], plist[x + 1] = plist[x + 1], plist[x]
            pdex[x], pdex[x + 1] = pdex[x + 1], pdex[x]
            swapped = True

pdex = ' '.join(map(str,pdex))
print pdex
