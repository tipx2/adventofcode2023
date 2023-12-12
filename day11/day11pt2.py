# part 2
with open("day11/input11.txt") as f:
  lines = f.readlines()

lines = [x.strip() for x in lines]

millionrows = []

for i in range(len(lines)):
  if all(lines[i][x] == "." for x in range(len(lines[i]))):
    millionrows.append(i)

millioncols = []

for i in range(len(lines[0])):
  if all(lines[x][i] == "." for x in range(len(lines))):
    millioncols.append(i)

galaxies = []

# find galaxies
bigvalue = 1000000
rowbonus = 0
colbonus = 0
for i in range(len(lines)):
  colbonus = 0
  rowbonus += (bigvalue - 1) * (i in millionrows)
  for j in range(len(lines[i])):
    colbonus += (bigvalue - 1) * (j in millioncols)
    if lines[i][j] == "#":
      galaxies.append((i + rowbonus, j + colbonus))

# perform manhatten distance pairing
distances = []
for g in galaxies:
  for h in galaxies:
    distances.append(abs(g[0] - h[0]) + abs(g[1] - h[1]))

print(int(sum(distances) / 2))
