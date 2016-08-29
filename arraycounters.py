#arraycounters

inputdata = """
10 3
3 2 1 2 3 1 1 1 1 3
"""
inputlist = [int(lmn) for lmn in inputdata.split()]
listlen = inputlist.pop(0)
listrange = inputlist.pop(0)
countarray = [0] * listrange

#for the number, add 1 to the index of the number in the counting array, print the array, c
#clear the array, repeat.  

for x in range(listlen):
	
	var1 = inputlist.pop(0)
	var2 = var1 - 1

	borg = countarray.pop(var2)
	borg = borg + 1

	countarray.insert(var2, borg)

countarray = ' '.join(map(str, countarray))
print countarray



