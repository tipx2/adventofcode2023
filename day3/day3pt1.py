with open("day3/input3.txt") as f:
  lines = f.readlines()

symbols = "$%&*-+=@#/"
def checkAround(lines, x, y):
  #print(lines[y][x])
  for i in [y + 1, y, y - 1]:
    for j in [x + 1, x, x - 1]:
      
      if i > len(lines)-1 or i < 0:
        continue
      if j > len(lines[i])-1 or j < 0:
        continue
      
      if lines[i][j] in symbols:
        return True
  return False


buffer = ""
ispart = False
x = 0
y = 0
total = 0

while y <= len(lines)-1:
  if lines[y][x].isdigit():
    buffer += lines[y][x]
    if not ispart:
      ispart = checkAround(lines, x, y)
  else:
    if ispart:
      #print(buffer)
      total += int(buffer)
    buffer = ""
    ispart = False
  
  x += 1
  if x > len(lines[y])-1:
    y += 1
    x = 0

print(total)