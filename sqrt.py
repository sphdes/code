#sqrt

pin = """
3
150 0
5 1
10 3
"""
plist = [int(x) for x in pin.split()]
pcase = plist.pop(0)

for x in range(pcase):
    num = plist.pop(0)
    rep = plist.pop(0)
    r = 1
    for x in range(rep):
        r = (float(r) + num / r) / 2
    print round(r,7),
