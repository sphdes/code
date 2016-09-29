#smoothing the weather

pin = """
7
32.6 31.2 35.2 37.4 44.9 42.1 44.1
"""
plist = [float(x) for x in pin.split()]
pcase = plist.pop(0)

print plist[0],

for x in range(1, int(pcase - 1)):
    y = x - 1
    z = x + 1
    ans = (plist[x] + plist[y] + plist[z]) / 3
    print ans,

print plist[-1]
