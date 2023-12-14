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


def moveAll(t):
  for i in range(len(oRocksArr)):
    while True:
      tempcoord = tuple([oRocksArr[i][0] + t[0], oRocksArr[i][1] + t[1]])
      withinlims = (0 <= tempcoord[0] <= len(lines)) and (0 <= tempcoord[1] <= len(lines[0]))
      if withinlims and tempcoord not in hashRocksArr and tempcoord not in oRocksArr:
          oRocksArr[i] = tempcoord
      else:
          break

def cycle():
  # north
  moveAll((-1, 0))
  # west
  moveAll((0, -1))
  # south
  moveAll((1, 0))
  # east
  moveAll((0, 1))

def getLoad():
  total = 0
  for i in range(len(oRocksArr)):
    total += len(lines) - oRocksArr[i][0]
  return total

counter = 0
states = {}

while True:
  
  state = tuple(oRocksArr)
  if state not in states.keys():
    states[state] = counter
  else:
    cyc = counter - states[state]
    break

  cycle()
  counter += 1
  


for x in range(1000000000%cyc - 1):
  cycle()

print(getLoad())