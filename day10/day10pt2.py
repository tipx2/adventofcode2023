with open("day10/input10.txt") as f:
  lines = f.readlines()

mainpath = {}

for i, line in enumerate(lines):
  if "S" in line:
    animaly = i
    animalx = line.find("S")

previous = (animaly + 1, animalx)

while True:
  currentchar = lines[animaly][animalx]
  storeprev = (animaly, animalx)
  
  mainpath[(animaly, animalx)] = currentchar
  
  if currentchar == "|":
    if previous == (animaly + 1, animalx):
      animaly -= 1
    elif previous == (animaly - 1, animalx):
      animaly += 1
      
  elif currentchar == "-":
    if previous == (animaly, animalx + 1):
      animalx -= 1
    elif previous == (animaly, animalx - 1):
      animalx += 1
      
  elif currentchar == "L":
    if previous == (animaly - 1, animalx):
      animalx += 1
    elif previous == (animaly, animalx + 1):
      animaly -= 1
      
  elif currentchar == "J":
    if previous == (animaly - 1, animalx):
      animalx -= 1
    elif previous == (animaly, animalx - 1):
      animaly -= 1
    
  elif currentchar == "7":
    if previous == (animaly + 1, animalx):
      animalx -= 1
    elif previous == (animaly, animalx - 1):
      animaly += 1
  
  elif currentchar == "F" or currentchar == "S":
    if previous == (animaly + 1, animalx):
      animalx += 1
    elif previous == (animaly, animalx + 1):
      animaly += 1
  
  if lines[animaly][animalx] == "S":
    break
  
  previous = storeprev

# we have mainpath now

areacount = 0

for y in range(len(lines)):
  counting = False
  for x, char in enumerate(lines[y]):
    if (y, x) in mainpath and char in "|LJ":
      counting = not counting
    elif counting and not (y, x) in mainpath:
      areacount += 1

print(areacount)