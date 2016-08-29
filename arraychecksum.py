#arraychecksum

inputdata = """

"""

inputlist = [int(lmn) for lmn in inputdata.split()]

listlen = inputlist.pop(0)

var1 = 0
var2 = 0

for x in range(listlen):
	y = inputlist[x]
	var1 = var2 + y
	var1 = var1 * 113
	var2 = var1 % 10000007

print var2
