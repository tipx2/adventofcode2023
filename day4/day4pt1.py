with open("day4/input4.txt") as f:
	lines = f.readlines()

total = 0
id = 1
for line in lines:
	it = 0
	#print(line)
	winning, selection = line.split(":")[1].split("|")
	winning = [int(x.strip()) for x in winning.split(" ") if x != ""]
	selection = [int(x.strip()) for x in selection.split(" ") if x != ""]
	for w in winning:
		if w in selection:
			#print(w)
			if it == 0:
				it = 1
			else:
				it *= 2
	#print(it, "\n")
	total += it
print(total)