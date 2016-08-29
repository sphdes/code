#sumofdigits

inputarray = """
133 249 167
57 260 87
183 133 190
319 96 128
357 106 89
312 230 61
177 66 189
146 208 192
260 217 127
298 127 173
102 222 140
38 259 114
"""

intarray = [int(lmn) for lmn in inputarray.split()]
numarray = []
sumarray = []
ansarray = []

while len(intarray) != 0:
	setA = intarray.pop(0)
	setB = intarray.pop(0)
	setC = intarray.pop(0)
	numA = setA * setB + setC
	numarray.append(numA)

while len(numarray) != 0:
	x = numarray[0]

	while x > 0:
		rmn = x % 10
		x = int(x / 10)
		sumarray.append(rmn)
	
		if x == 0:
			sumA = sum(sumarray)
			ansarray.append(sumA)
			del sumarray[:]
			numarray.pop(0)
		else:
			continue
		
ansarray = ' '.join(map(str,ansarray))
print ansarray
