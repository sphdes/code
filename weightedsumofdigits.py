#weightedsumofdigits

inputdata = """
3
9 15 1776
"""

intlist = [int(lmn) for lmn in inputdata.split()]
digitlist = []
digitproduct = []
listlen = intlist.pop(0)

def borg(var):
	x = intlist[var]
	while x > 0:
		rmn = x % 10
		x = int(x / 10)
		digitlist.insert(0, rmn)
		
		if x == 0:
			for y in range(0, len(digitlist)):
				z = (y + 1) * digitlist[y]
				digitproduct.append(z)

			print sum(digitproduct),
			del digitproduct[:]
			del digitlist[:]

		else: 
			continue

for nums in range(0, listlen):
	borg(nums)

