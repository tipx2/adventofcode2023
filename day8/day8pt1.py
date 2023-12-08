with open("day8/input8.txt") as f:
  lines = f.read()

leftright, lines = lines.split("\n\n")
lines = lines.split("\n")

pathsdict = {}
for line in lines:
  line = line.split(" = ")
  pathsdict[line[0]] = [h.strip() for h in line[1].strip("()").split(",")]

currpos = "AAA"
currinst = 0
lr = 0
while currpos != "ZZZ":
  if leftright[currinst % len(leftright)] == "L":
    lr = 0
  elif leftright[currinst % len(leftright)] == "R":
    lr = 1
  currpos = pathsdict[currpos][lr]
  currinst += 1

print(currinst)