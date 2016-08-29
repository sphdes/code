#code abbey problem 3
stndinput = '''
179529 801885
19854 477077
24517 300170
141202 739279
10909 763309
282298 535973
196422 970601
65450 398691
949409 930917
968630 154163
902832 830770
353389 383356
338289 167720
54953 772138
174474 437138
'''
list1 = [int(cab) for cab in stndinput.split()]
setA = []
setB = []
list2 = []

def split ():
	while len(list1) != 0:
		popA = list1.pop(0)
		setA.append(popA)
		popB = list1.pop(0)
		setB.append(popB)

def suminput():
	while len(setA) != 0: 
		suma = setA.pop(0)
		sumb = setB.pop(0)
		prob = suma + sumb
		list2.append(prob)
		
split()
suminput()
list2 = ' '.join(map(str, list2))
print list2
