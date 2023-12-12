from functools import cache
with open("day12/input12.txt") as f:
    lines = f.readlines()

@cache
def checkLineGrouping(s : str, g : tuple, hash_count=0):
  if not s:
    return (len(g) == 0 and hash_count == 0) or (len(g) == 1 and g[0] == hash_count)

  total = 0
  if s[0] == "?":
    total += checkLineGrouping("#" + s[1:], g, hash_count) + checkLineGrouping("." + s[1:], g, hash_count)
  elif s[0] == ".":
    if hash_count > 0:
      if hash_count == g[0]:
          total += checkLineGrouping(s[1:], g[1:], 0)
      else:
        return 0
    else:
      total += checkLineGrouping(s[1:], g, 0)
  elif s[0] == "#":
    hash_count += 1
    if len(g) == 0 or hash_count > g[0]:
      return 0
    else:
      total += checkLineGrouping(s[1:], g, hash_count)
  return total
  

def unfold(s, g):
  s = "?".join([s] * 5)
  g = g * 5
  return s, g

total = 0
for z, line in enumerate(lines):
    springs, grouping = line.split(" ")
    grouping = tuple(int(x.strip()) for x in grouping.split(","))
    
    springs, grouping = unfold(springs, grouping)
    total += checkLineGrouping(springs, grouping)

print(total)