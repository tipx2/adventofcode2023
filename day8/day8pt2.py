from math import lcm
with open("day8/input8.txt") as f:
  lines = f.read()


leftright, lines = lines.split("\n\n")
lines = lines.split("\n")

pathsdict = {}
for line in lines:
  line = line.split(" = ")
  pathsdict[line[0]] = [h.strip() for h in line[1].strip("()").split(",")]


currposes = {key:key for key in pathsdict.keys() if key.endswith("A")}
currposesvalues = {pos: 0 for pos in currposes.keys()}

currinst = 0
lr = 0

while 0 in currposesvalues.values():
  
  if leftright[currinst % len(leftright)] == "L":
    lr = 0
  elif leftright[currinst % len(leftright)] == "R":
    lr = 1

  for key in currposes.keys():
    if currposes[key].endswith("Z"):
      continue
    currposes[key] = pathsdict[currposes[key]][lr]
    if currposes[key].endswith("Z"):
      currposesvalues[key] = currinst + 1
  print(currposesvalues)
  currinst += 1

print(lcm(*currposesvalues.values()))