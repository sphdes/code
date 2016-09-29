#josephus problem attempt 2

pin = """
71 15
"""
plist = [int(x) for x in pin.split()]

n = plist[0]
k = plist[1]
p = 1
par = range(n)

for x in range(n - 1):
    p = (p + (k - 1)) % len(par)
    par.pop(p)

print par[0]
