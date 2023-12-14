from copy import deepcopy
with open("day14/input14.txt") as f:
  lines = f.readlines()

def debugDraw(rocksArr, hashArr):
  for i in range(len(lines)):
    for j in range(len(lines[0])):
      if [i, j] in rocksArr:
        print("O", end="")
      elif[i, j] in hashArr:
        print("#", end="")
      else:
        print(".", end="")
    print()

oRocksArr = []
hashRocksArr = []

for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "O":
      oRocksArr.append([i, j])
    elif lines[i][j] == "#":
      hashRocksArr.append([i, j])

#debugDraw(oRocksArr, hashRocksArr)
#print()

total = 0
for i in range(len(oRocksArr)):
  
  for j in range(len(lines)):
    tempcoord = oRocksArr[i][0] - 1

    if tempcoord != -1 and [tempcoord, oRocksArr[i][1]] not in hashRocksArr and [tempcoord, oRocksArr[i][1]] not in oRocksArr:
      oRocksArr[i][0] -= 1
    else:
      break

  
  total += len(lines) - oRocksArr[i][0]

#debugDraw(oRocksArr, hashRocksArr)

print(total)
  