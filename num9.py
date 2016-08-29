#codeabbeynum9
probinput = """
30 552 240 129 505 197 377 286 94 153 576 302 70 285 409 120 90 133 528 507 323 446 289 346 283 209 578 420 218 151 85
"""

fahinput = list(map(int,probinput.split()))
ansarray = []
arng = fahinput.pop(0)

for temp in fahinput:
        conv = float(temp - 32) * (float(5) / float(9))
        ansarray.append(int(round(conv)))

ansarray = ' '.join(map(str, ansarray))

print ansarray
