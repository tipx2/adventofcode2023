with open("day15/input15.txt") as f:
  line = f.read()

line = line.split(",")
currvaluesum = []

for instruction in line:
  currvalue = 0
  for chara in instruction:
    currvalue += ord(chara)
    currvalue *= 17
    currvalue = currvalue % 256
  currvaluesum.append(currvalue)


print(currvaluesum)
print(sum(currvaluesum))