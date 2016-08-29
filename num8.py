#codyabbeynum8

probinput = """

"""

probarray = [float(elm) for elm in probinput.split()]
ansarray = []

def borg (array):
    while len(array) != 0:
         partA = float(array.pop(0))
         partB = float(array.pop(0))
         result = int(partA) // int(partB)
         if (float(partA)/float(partB)) - result == 0.5:
             result = result + 1
             ansarray.append(result)
         elif (float(partA)/float(partB)) - result > 0.5:
             result = result + 1
             ansarray.append(result)
         else:
             ansarray.append(result)

borg(probarray)

ansarray = ' '.join(map(str,ansarray))

print ansarray
