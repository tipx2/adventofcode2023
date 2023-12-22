with open("day22/input22.txt") as f:
  lines = [x.strip() for x in f.readlines()]

def checkCollision(block, bricks):
  for brick in bricks:
    if block in brick:
      return True
  else:
    if block[2] <= 1:
      return True
  return False

def fallDown(bricks):
  for i, brick in enumerate(bricks):
    if i % 200 == 0:
      print("AV", i)
    lowest_z_blocks = [b for b in brick if b[2] == brick[0][2]]
    test_blocks = [(z[0], z[1], z[2] - 1) for z in lowest_z_blocks]
    while True:
      for z_block in test_blocks:
        if checkCollision(z_block, bricks):
          break
      else:
        test_blocks = [(z[0], z[1], z[2] - 1) for z in test_blocks]
        continue
      break

    fallendiff = lowest_z_blocks[0][2] - test_blocks[0][2] - 1
    bricks[i] = [(x[0], x[1], x[2] - fallendiff) for x in bricks[i]]
  

bricks = []
for line in lines:
  ranges = []
  firstblock, lastblock = [[int(y) for y in x.split(",")] for x in line.split("~")]
  for i in range(len(firstblock)):
      if firstblock[i] != lastblock[i]:
        for x in range(abs(firstblock[i] - lastblock[i]) + 1):
          new_range = tuple(firstblock[:i] + [firstblock[i] + x] + firstblock[i + 1:])
          ranges.append(new_range)
        break
  if len(ranges) == 0: # if there is no change between firstblock and lastblock
    ranges.append(tuple(firstblock))
  
  bricks.append(sorted(ranges, key=lambda x: x[2]))

bricks = sorted(bricks, key=lambda x: x[0][2])

fallDown(bricks)

def isSupporting(b1, b2): # not real name
  for block in b1:
    if (block[0], block[1], block[2] + 1) in b2:
      return True
  return False

def willFall(b2, b1):
  test_blocks = [(z[0], z[1], z[2] - 1) for z in b1]
  test_blocks = [b for b in test_blocks if b[2] == test_blocks[0][2]]
  for brick in bricks:
    if brick == b2:
      continue
    for block in test_blocks:
      if block in brick:
        return False
  return True

total = 0
for i in range(len(bricks)):
  if i % 200 == 0:
    print("AV2", i)
  for j in range(len(bricks)):
    if isSupporting(bricks[i], bricks[j]) and willFall(bricks[i], bricks[j]):
      break
  else:
    # print(bricks[i])
    total += 1

print(total)