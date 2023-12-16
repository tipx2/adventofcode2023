import sys
with open("day16/input16.txt") as f:
  lines = f.read().strip().split("\n")

def addCoords(a, b):
  return (a[0] + b[0], a[1] + b[1])

def debugDraw(s):
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if (i, j) in [(x[0],x[1]) for x in s]:
        print("#", end="")
      else:
        print(".", end="")
    print()

sys.setrecursionlimit(0x7FFFFFFF)

seen = set()

# some reddit help
def makePath(row, col, xdir, ydir):
    if (row, col, xdir, ydir) in seen or row < 0 or col < 0 or row >= len(lines) or col >= len(lines[0]):
        return
    seen.add((row, col, xdir, ydir))
    if lines[row][col] == "/":
      makePath(row - ydir, col - xdir, -ydir, -xdir)
    elif lines[row][col] == "\\":
      makePath(row + ydir, col + xdir, ydir, xdir)
    elif lines[row][col] == "-" and xdir:
      makePath(row, col+1, 0, 1)
      makePath(row, col-1, 0, -1)
    elif lines[row][col] == "|" and ydir:
      makePath(row+1, col, 1, 0)
      makePath(row-1, col, -1, 0)
    else:
      makePath(row+xdir, col+ydir, xdir, ydir)


makePath(0, 0, 0, 1)
seen = set((x[0],x[1]) for x in seen)
print(len(seen))

#debugDraw(seen)
