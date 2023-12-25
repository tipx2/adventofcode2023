with open("day21/input21.txt") as f:
  lines = [x.strip() for x in f.readlines()]

rowlen = len(lines)
collen = len(lines[0])

rocks = set()
walkable_positions = []

for i in range(rowlen):
  for j in range(collen):
    if lines[i][j] == "S":
      walkable_positions.append((i, j))
    elif lines[i][j] == "#":
      rocks.add((i, j))


def debugDraw(rocks, walk_positions):
  for x in range(rowlen):
    for y in range(collen):
      if (x, y) in rocks:
        print("#", end="")
      elif (x, y) in walk_positions:
        print("O", end="")
      else:
        print(".", end="")
    print()
  
quad = []
for x in range(1, 2319084320989502980):
  new_positions = []
  for position in walkable_positions:
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      new_pos = (position[0] + d[0], position[1] + d[1])
      if (new_pos[0] % rowlen,  new_pos[1] % collen) not in rocks:
        new_positions.append(new_pos)

  walkable_positions = list(set(new_positions))
  
  if x%collen == 26501365%collen:
    quad.append(len(walkable_positions))
    if len(quad) == 3:
      break

# assemble quadratic below
def f(n):
  a0 = quad[0]
  a1 = quad[1]
  a2 = quad[2]
  
  b0 = a0
  b1 = a1-a0
  b2 = a2-a1
  return b0 + b1*n + (n*(n-1)//2)*(b2-b1)

print(f(26501365//collen))