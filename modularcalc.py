#modularcalculator

inputdata = """

"""

inputlist = inputdata.split()
oplist = []
numlist = []
val = int(inputlist.pop(0))

while len(inputlist) != 0:
    oplist.append(inputlist.pop(0))
    numlist.append(int(inputlist.pop(0)))

while len(numlist) != 0:
    op = oplist.pop(0)
    num = numlist.pop(0)

    if op == "+":
        val += num
    elif op == "-":
        val -= num
    elif op == "*":
        val *= num
    elif op == "/":
        val /= num
    elif op == "%":
        val %= num

print val
