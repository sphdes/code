#fibonacci sequence

pin = """
5
610
34
0
1346269
10946
"""
plist = [int(x) for x in pin.split()]
pcase = plist.pop(0)

for x in range(pcase):
    a = 0
    b = 1
    fibin = 0
    switch = True
    while switch:
        switch = False
        if plist[x] != a:
            a, b = b, (a + b)
            switch = True
            fibin += 1
        elif plist[x] == a:
            print fibin,
