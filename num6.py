#codeabbeyproblem6

probinput="""
4117 974
10765 1774
5263 1074
-5128770 -4807042
12843 560
2145043 925
10431 1282
13867 1274
9448779 367
-4227030 -4936821
19351 420
6934232 436
"""

basic = [int(elm) for elm in probinput.split()]
listAns = []

def prob6():
	while len(basic) != 0:
		set1 = basic.pop(0)
		set2 = basic.pop(0)
		div1 = int(set1 / set2)
		listAns.append(div1)
		

prob6()

listAns = ' '.join(map(str,listAns))

print listAns

