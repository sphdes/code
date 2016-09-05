#modulotimedifference
indata = """
3
1 0 0 0 2 3 4 5
5 3 23 22 24 4 20 45
8 4 6 47 9 11 51 13
"""
inlist = [int(x) for x in indata.split()]
casenum = inlist.pop(0)

datea = []
dateb = []

def conv(a,b,c,d):
    return (((((a * 24  + b) * 60) + c) * 60) + d)

def reconv(x):
    a = x % 60
    b = ((x - a)/60) % 60
    c = ((((x - a)/60) - b)/60) % 24
    d = (((((x - a)/60) - b)/60) - c) / 24
    print "(%d %d %d %d) " % (d,c,b,a)

for y in range(casenum):
    for x in range(4):
        datea.append(inlist.pop(4-x))
        dateb.append(inlist.pop(0))

    rem = conv(*datea) - conv(*dateb)
    reconv(rem)

    del datea[:]
    del dateb[:]
