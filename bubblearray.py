#bubble in array

pin = """
1 4 3 2 6 5 -1
"""
plist = [int(x) for x in pin.split()]
plist.pop()
plen = len(plist) - 1
scount = 0
var1 = 0
var2 = 0

while plist[-1] != max(plist):
    for x in range(plen):
        if plist[x] == max(plist) or plist[x] > plist[x + 1]:
            plist[x] , plist[x + 1] = plist[x + 1] , plist[x]
            scount += 1

for x in range(len(plist)):
	var1 = var2 + plist[x]
	var1 = var1 * 113
	var2 = var1 % 10000007

print "%d %d" % (scount, var2)
