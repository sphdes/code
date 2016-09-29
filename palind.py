#palindromes

pin = '''
3
Stars
O, a kak Uwakov lil vo kawu kakao!
Some men interpret nine memos
'''
plist = [x for x in pin.split('\n')]
plist = plist[1:-1]
pcase = int(plist.pop(0))

for x in range(pcase):
    aline = [y.lower() for y in plist[x] if y.isalpha()]
    reverse = list(reversed(aline))

    if aline == reverse:
        print 'Y',
    else:
        print 'N',
