#pythagorean theorem

pin = """
3
6 8 9
9 12 15
16 12 22
"""
pcase = int(input())
plist = [int(x) for x in input().split()]

for x in range(pcase):
    lis = plist[0:3]
    c = lis.pop(lis.index(max(lis)))
    a,b = lis[0:2]

    a = a*a
    b = b*b
    c = c*c

    if a + b == c:
        print "R",
    elif a + b > c:
        print "A",
    else:
        print "O",

    del plist[0:3]
