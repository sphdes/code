#codeabbeynum7
probinput = """

"""
intarray = [int(elm) for elm in probinput.split()]
ansarray = []

def borg():
    bigint = intarray.pop(0)
    nextint = intarray.pop(0)
    smallint = bigint
    while len(intarray) != 0:
        if bigint >= nextint:
            nextint = intarray.pop(0)
            if nextint < smallint:
                smallint = nextint
            else:
                pass
        else:
            bigint = nextint
            nextint = intarray.pop(0)
    ansarray.append(bigint)
    ansarray.append (smallint)

borg()

ansarray = ' '.join(map(str,ansarray))

print ansarray
