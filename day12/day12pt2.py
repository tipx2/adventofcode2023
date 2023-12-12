from functools import lru_cache
with open("day12/test12.txt") as f:
    lines = f.readlines()

@lru_cache(maxsize=None)
def checkLineGrouping(s : str, g : tuple, hash_count=0, group_count=0):
  # if we are all out, return 1
  if s == "":
    if group_count == len(g):
      return 1
    else:
      return 0
  # if it's ever invalid, return 0
  # invalid cases:
    # if amount of #s in s is greater than sum of g
    # if hash_count is greater than g[group_count]
    # if the length of g is equal to group_count and there is still #s in s
  if group_count > len(g)-1:
    return 0
  if s.count("#") > sum(g):
    return 0
  if hash_count > g[group_count]:
    return 0
  if (len(g) == group_count and "#" in s):
    return 0
  # --- go through each character and keep track of what group we are on ---
  for i in range(len(s)):
    if s[i] == "?":
      # if we hit a ?, split and recurse
      return checkLineGrouping("#" + s[1:], g, hash_count, group_count) + checkLineGrouping("." + s[1:], g, hash_count, group_count)
    elif s[i] == ".":
      # if we hit a ., shave it off, increment group_count if the hash_count is not 0, reset hash_count, recurse
      if hash_count > 0:
        group_count += 1
        hash_count = 0
      return checkLineGrouping(s[1:], g, hash_count, group_count)
    elif s[i] == "#":
      # if we hit a #, increment hash_count, shave it off, recurse
      return checkLineGrouping(s[1:], g, hash_count + 1, group_count)
  

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