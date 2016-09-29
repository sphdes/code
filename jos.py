#josephus problem

pin = """
63 16
"""
plist = [int(x) for x in pin.split()]

n = plist[0]
k = plist[1]
parr = range(1, n + 1)
p = k - 1

while len(parr) > 1:

    if p >= len(parr):
        p = p - len(parr)
        print p
        print len(parr)
        print parr
        parr = filter(lambda z: z != 'n', parr)

    if p >= len(parr):
        p = (p + k) % len(parr)

    if len(parr) == 1:
        break

    if type(parr[p]) is str:
        p = p + 1

    else:
        parr[p] = str('n')
        p = p + k

print parr[0]
