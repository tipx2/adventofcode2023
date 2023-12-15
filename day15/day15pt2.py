import re
with open("day15/input15.txt") as f:
  line = f.read()

line = line.split(",")

def getHASHValue(instruction):
  currvalue = 0
  for chara in instruction:
    currvalue += ord(chara)
    currvalue *= 17
    currvalue %= 256
  return currvalue

def getPower(h):
  total = 0
  for key in h.keys():
    for label in h[key].keys():
      labelpos = list(h[key].keys()).index(label)
      total += (key + 1) * (labelpos + 1) * h[key][label]
  return total
      


hashmap = {} # dict of dicts
for instruction in line:
  label = re.match("[A-Za-z]+", instruction)[0]
  box = getHASHValue(label)
  if "-" in instruction:
    if box not in hashmap:
      hashmap[box] = {}
    elif label in hashmap[box].keys():
      del hashmap[box][label]
  elif "=" in instruction:
    if box in hashmap:
      hashmap[box][label] = int(instruction.split("=")[1])
    else:
      hashmap[box] = {label: int(instruction.split("=")[1])}

print(getPower(hashmap))