#gcd

indat = """
2
2 3
4 10
"""

inlist = [int(x) for x in indat.split()]
casen = inlist.pop(0)
for x in range(casen):
    a , b = inlist[0:2]
    m = 0
    L = a * b
    while a != b:
        m = abs(a - b)
        if a > b:
            a = m
        else:
            b = m
    print "(%d %d)" % (a , L/a),
    del inlist[0:2]
