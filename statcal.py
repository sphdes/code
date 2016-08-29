#statcal

res = 0

def calc():
	x = input('Enter desired stat value ')

	if 0 <= x <= 50:
		res = x + (x/5)

	elif 51 <= x <= 150:
		res = x + 10 + ((x-50)/4)

	elif 151 <= x <= 300:
		res = x + 35 + ((x-150)/3)

	elif 301 <= x <= 500:
		res = x + 85 + ((x-300)/2)

	else:
		res = x - 315

	print res
	rerun()

def rerun():
	restart = raw_input("Rerun? y/n: ")
	if restart == "y":
		calc()
	if restart == "n":
		print "Calc ended"

calc()
