#linfunc

indat = """
2
0 0 1 1
1 0 0 1
"""

indat = [int(x) for x in indat.split()]
cn = indat.pop(0)

for x in range(cn):
    ldat = indat[0:4]
    del indat[0:4]
    a,b,c,d = ldat[0:4]
    s = (d - b)/(c - a)
    v = b - (a * s)
    print "(%d %d)" % (s, v),
