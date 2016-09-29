#rotatestring

pin = """
2
3 forwhomthebelltolls
-6 verycomplexnumber
"""

plist = [x for x in pin.split()]
pcase = int(plist.pop(0))

for x in range(pcase):
    num = int(plist.pop(0))
    cha = str(plist.pop(0))
    len1 = len(cha)
    len2 = len(cha) - abs(num)

    if num > 0:
        i = cha[0:num]
        j = cha[num:len1]
        cha = j + i

    elif num < 0:
        i = cha[0:len2]
        j = cha[len2:len1]
        cha = j + i

    print cha,
