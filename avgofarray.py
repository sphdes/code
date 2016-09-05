#averageofanarray

probinput = """
3
2 3 7 0
20 10 0
1 0
"""
avgarray = []

inputlist = [int(x) for x in probinput.split()]

listlen = inputlist.pop(0)

while len(inputlist) != 0:

	popval = inputlist.pop(0)
	avgarray.append(popval)

	if inputlist[0] == 0:
		inputlist.pop(0)
		avg = int(round(float(sum(avgarray)) / len(avgarray)))
		print avg,
		del avgarray[:]

	else: 
		continue