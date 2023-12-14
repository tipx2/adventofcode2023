with open("day13/input13.txt") as f:
		lines = f.read()

lines = [x.split("\n") for x in lines.split("\n\n")]

def isReflect(box, line):
		for i in range(len(box)):
				if line + i >= len(box) or (line - i + 1) < 0: # if we hit the edge, the whole thing is confirmed reflected in this line
						return True
				elif box[line + i] != box[line - i + 1]: # if we come across a none reflecting line, this is not where it reflects
						return False

def checkAllRefs(box, originalref=(-1, True)):
		for l in range(len(box)-1):
				if isReflect(box, l) and originalref != (l, True):
						return (l, True)

		rotated = list(map("".join, zip(*reversed(box))))
		for l in range(len(rotated)-1):
				if isReflect(rotated, l) and originalref != (l, False):
						return (l, False)

		return -1

def findSmudge(box):
		originalref = checkAllRefs(box)
		possiblepatterns = []
		for j in range(len(box)):
				for k in range(len(box[j])):
						flip = "#" if box[j][k] == "." else "."
						exrow = box[j][:k] + flip + box[j][k+1:]
						extable = box[:j] + [exrow] + box[j+1:]

						checkrefs = checkAllRefs(extable, originalref)
						if checkrefs != -1:
								if checkrefs[1]:
										return 100 * (checkrefs[0] + 1)
								else:
										return checkrefs[0] + 1
		return -1




total = 0
for i in range(len(lines)): # in each group
		d = findSmudge(lines[i])
		total += d

print(total)