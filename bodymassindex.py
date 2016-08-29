#bodymassindex
#bmi = weight/height^2
#weight = kg height = meters
#underweight - bmi < 18.5
#normal - 18.5 <= bmi < 25.0
#overweight - 25.0 <= bmi < 30.0
#obese - 30.0 <= bmi

probinput = """
43 1.14
60 1.39
80 2.58
113 2.66
85 1.66
76 1.68
110 1.88
118 2.43
94 2.12
113 2.51
76 1.90
103 1.79
87 1.94
86 2.48
103 1.74
60 1.35
96 2.00
88 2.35
86 1.89
70 2.24
62 1.37
98 2.56
89 1.75
79 2.09
45 1.46
83 1.82
"""
setweight = []
setheight = []
setbmi = []

inputdata = [float(lmn) for lmn in probinput.split()]

while len(inputdata) != 0:
	setweight = inputdata.pop(0)
	setheight = inputdata.pop(0)
	setbmi = setweight / (setheight * setheight)
		
	if setbmi < 18.5:
		print "under",
	elif 18.5 <= setbmi < 25.0:
		print "normal",
	elif 25.0 <= setbmi < 30.0:
		print "over",
	elif 30.0 <= setbmi:
		print "obese",




