with open("day14/input14.txt") as f:
  lines = [x.strip() for x in f.readlines()]

def moveAll(lines):
  for i in range(len(lines)):
    while lines[i] != lines[i].replace("O.", ".O"):
      lines[i] = lines[i].replace("O.", ".O")
  return lines
  
def rotate(lines):
  return list(map("".join, zip(*reversed(lines))))

def cycle(l):
  for _ in range(4):
    l = moveAll(rotate(l))
  return l

def getLoad(l):
  total = 0
  for i in range(len(l)):
    total += l[i].count("O") * (len(l) - i)
  return total

states = {}
for k in range(1_000_000_000):
  lines = cycle(lines)
  currstate = "".join(lines)
  
  if currstate in states.keys():
    loop_size = k - states[currstate]
    loop_start = states[currstate]
    break
  else:
    states[currstate] = k

step = (1_000_000_000 - (loop_start + 1)) % loop_size

for j in range(step):
  lines = cycle(lines)

print(getLoad(lines))