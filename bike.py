#bicycle race

pin = """
2
10 1 1
20 1 2
"""

plist = [int(x) for x in pin.split()]
pcase = plist.pop(0)

for x in range(pcase):
    s,a,b = plist[0:3]
    c = (float(s) / (a + b)) * a
    print c,
    del plist[0:3]
