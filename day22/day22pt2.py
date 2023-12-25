with open("day22/input22.txt") as f:
  lines = [x.strip() for x in f.readlines()]

def rangeOverlap(range1, range2):
  return (max(range1[0], range2[0]), min(range1[1], range2[1]))


def checkCollision(brick, bricks):
  if brick[0][2] < 1:
    return True
  for _, otherbrick in bricks:
    for i in range(3):
      # brick = ((x, y, z), (x, y, z))
      overlap = rangeOverlap((otherbrick[0][i], otherbrick[1][i]), (brick[0][i], brick[1][i]))
      if overlap[0] > overlap[1]:
        break
    else:
      return True
  return False

def fallDown(bricks):
  for i, (j, brick) in enumerate(bricks):
    test_brick = ((brick[0][0], brick[0][1], brick[0][2] - 1),(brick[1][0], brick[1][1], brick[1][2] - 1))
    while not checkCollision(test_brick, [b for b in bricks if b != (j, brick)]):
      test_brick = ((test_brick[0][0], test_brick[0][1], test_brick[0][2] - 1),(test_brick[1][0], test_brick[1][1], test_brick[1][2] - 1))

    fallendiff = brick[0][2] - test_brick[0][2] - 1
    bricks[i] = (j, ((brick[0][0], brick[0][1], brick[0][2] - fallendiff),(brick[1][0], brick[1][1], brick[1][2] - fallendiff)))

bricks = []
for line in lines:
  firstblock, lastblock = [tuple(int(y) for y in x.split(",")) for x in line.split("~")]
  bricks.append((firstblock, lastblock))

bricks = [(i, brick) for i, brick in enumerate(bricks)]

bricks = sorted(bricks, key=lambda x: x[1][0][2])
fallDown(bricks)
# print(bricks)

# funny solution

total = 0
for i in range(len(bricks)):
  if i % 200 == 0:
    print("AV", i)
  
  brickscopy = bricks.copy()
  del brickscopy[i]
  double_brickscopy = brickscopy.copy()
  fallDown(brickscopy)
  total += len(set(brickscopy).difference(set(double_brickscopy)))

print(total)