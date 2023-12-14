with open("day13/input13.txt") as f:
		lines = f.read()

lines = [x.split("\n") for x in lines.split("\n\n")]

def isReflect(box, line):
		for i in range(len(box)):
				if line + i >= len(box) or (line - i + 1) < 0: # if we hit the edge, the whole thing is confirmed reflected in this line
						return True
				elif box[line + i] != box[line - i + 1]: # if we come across a none reflecting line, this is not where it reflects
						return False

def checkAllRefs(box):
		for l in range(len(box)-1):
				if isReflect(box, l):
						return (l, True)

		rotated = list(map("".join, zip(*reversed(box))))
		for l in range(len(rotated)-1):
				if isReflect(rotated, l):
						return (l, False)

		return -1

total = 0
for i in range(len(lines)): # in each group
		ref = checkAllRefs(lines[i])

		total += ref[0] + 1 if not ref[1] else 100 * (ref[0] + 1)

print(total)