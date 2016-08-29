#triangles

inputdata = """

"""

inputlist = [int(lmn) for lmn in inputdata.split()]

listlen = inputlist[0]
del inputlist[0]

for x in range(listlen):

	a = inputlist.pop(0)
	b = inputlist.pop(0)
	c = inputlist.pop(0)

	if a + b > c:

		if a + c > b:
		
			if b + c > a:
		
				print "1",

			else: 
				print "0",
		else: 
			print "0",
	else: 
		print "0",	