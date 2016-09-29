#neumann's random generator

pin = """
3
0001 4100 5761
"""
plist = [int(x) for x in pin.split()]
pcase = plist.pop(0)

def rng(x):
    a = plist[x]
    alist = [a]
    a = int(((a**2)/100)%10000)
    alist.append(a)
    c = 1
    while c < 2:
        b = a
        a = int(((a**2)/100)%10000)
        alist.append(a)
        c = alist.count(a)
    else:
        print len(alist) - 1
        del alist[:]

for x in range(pcase):
    rng(x)
