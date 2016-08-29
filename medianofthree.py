#codeabbey median of three

probinput = """
7 6 229
794 795 805
60 825 779
519 530 3
55 41 46
245 154 244
167 170 244
7 49 6
412 368 437
13 18 25
163 140 135
329 219 50
109 99 89
8 18 5
4 102 172
11 9 481
680 103 98
4 427 1
786 690 688
1007 1499 338
739 38 76
580 587 592
708 531 9
77 85 81
589 137 144
10 9 107
"""

probarray = [int(elm) for elm in probinput.split()]
final = []
compare = []

while len(probarray) != 0:
	set1 = probarray.pop(0)
	set2 = probarray.pop(0)
	set3 = probarray.pop(0)
	compare.append(set1)
	compare.append(set2)
	compare.append(set3)
	max_val= max(compare)
	min_val = min(compare)

	if (set1 == max_val and set2 == min_val) or (set2 == max_val and set1 == min_val):
		final.append(set3)
		del compare[:]

	elif (set2 == max_val and set3 == min_val) or (set3 == max_val and set2 == min_val):
		final.append(set1)
		del compare[:]

	else:
		final.append(set2)
		del compare[:]

final = ' '.join(map(str, final))

print final

