#codeabbeyproblem5

probinput="""

"""

basic = [int(elm) for elm in probinput.split()]
listAns = []

def prob4():
	while len(basic) != 0:
		set1 = basic.pop(0)
		set2 = basic.pop(0)
		set3 = basic.pop(0)
		if set1 < set2 and set1 < set3:
			listAns.append(set1)
		elif set2 < set1 and set2 < set3:
			listAns.append(set2)
		else:
			listAns.append(set3)
		

prob4()

listAns = ' '.join(map(str,listAns))

print listAns

