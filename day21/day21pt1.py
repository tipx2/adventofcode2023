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
  

# each step, look in all 4 directions of each current step and add them all to a new array if they are not a rock
# then set walkable positions to that array
# repeat for n times

for x in range(64):
  if x % 8 == 0:
    print("av", x)
  new_positions = []
  for position in walkable_positions:
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      new_pos = (position[0] + d[0], position[1] + d[1])
      if (0 <= new_pos[0] < rowlen) and (0 <= new_pos[1] < collen) and (new_pos not in rocks):
        new_positions.append(new_pos)
  walkable_positions = list(set(new_positions))

#debugDraw(rocks, walkable_positions)

print(len(walkable_positions))