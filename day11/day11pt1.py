# part 1
with open("day11/input11.txt") as f:
  lines = f.readlines()

lines = [x.strip() for x in lines]

# double rows
for i in range(len(lines) - 1, 0, -1):
  if all(lines[i][x] == "." for x in range(len(lines[i]))):
    lines.insert(i, lines[i])

# double columns
for i in range(len(lines[0]) - 1, 0, -1):
  if all(lines[x][i] == "." for x in range(len(lines))):
    for j in range(len(lines)):
      lines[j] = lines[j][:i] + "." + lines[j][i:]

# stretch has now been performed

galaxies = []

# find galaxies
for i in range(len(lines)):
  for j in range(len(lines[i])):
    if lines[i][j] == "#":
      galaxies.append((i, j))

# perform manhatten distance pairing
distances = []
for g in galaxies:
  for h in galaxies:
    distances.append(abs(g[0] - h[0]) + abs(g[1] - h[1]))

print(int(sum(distances) / 2))
