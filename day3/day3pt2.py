with open("day3/input3.txt") as f:
  lines = f.readlines()

geardict = {}

def checkAround(y, x, lines, buff):
  for i in [y + 1, y, y - 1]:
    for j in [x + 1, x, x - 1]:

      if i > len(lines)-1 or i < 0:
        continue
      if j > len(lines[i])-1 or j < 0:
        continue
      
      if lines[i][j] == "*":
        if tuple([i, j]) in geardict:
          geardict[tuple([i, j])].append(buff)
        else:
          geardict[tuple([i, j])] = [buff]
        return True
  return False

buffer = ""
buffered_coords = []

x = 0
y = 0
isgear = False

while y <= len(lines)-1:
  if lines[y][x].isdigit():
    buffer += lines[y][x]
    buffered_coords.append([y, x])
  else:
    for n in buffered_coords:
      isgear = checkAround(n[0], n[1], lines, int(buffer))
      if isgear:
        break
    
    buffered_coords.clear()
    buffer = ""
    isgear = False
  
  # incrementing stuff
  x += 1
  if x > len(lines[y])-1:
    y += 1
    x = 0

total = 0
for d in geardict.values():
  if len(d) == 2:
    total += d[0] * d[1]
    
print(total)