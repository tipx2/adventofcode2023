with open("day9/input9.txt") as f:
  lines = f.readlines()

def findDiff(l):
  diffarr = []
  for i in range(1, len(l)):
    diffarr.append(l[i] - l[i-1])
  return diffarr

total = 0
for line in lines:
  line = [int(x) for x in line.split(" ")]
  
  diffs = [line]
  while True: # do while loop
    diffs.append(findDiff(diffs[-1]))
    if all(num == 0 for num in diffs[-1]):
      break
  
  diffs = list(reversed(diffs))
  
  sub = diffs[1][0]
  for x in range(2, len(diffs)):
    diffs[x].insert(0, diffs[x][0] - sub)
    sub = diffs[x][0]
  
  total += diffs[-1][0]

print(total)