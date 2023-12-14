with open("day14/test14.txt") as f:
  lines = f.readlines()

oRocksArr = []
hashRocksArr = []

for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "O":
      oRocksArr.append((i, j))
    elif lines[i][j] == "#":
      hashRocksArr.append((i, j))

total = 0
for i in range(len(oRocksArr)):
  while not(oRocksArr[i][0] == 0 or oRocksArr[i] in hashRocksArr or oRocksArr[i] in oRocksArr) :
    oRocksArr[i] = (oRocksArr[i][0] - 1, oRocksArr[i][1])
  
  total += len(lines) - oRocksArr[i][0]
  
print(total)
  