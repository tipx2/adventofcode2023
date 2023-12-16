import sys
with open("day16/input16.txt") as f:
  lines = f.read().strip().split("\n")

def addCoords(a, b):
  return (a[0] + b[0], a[1] + b[1])

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

def getEnergy(a, b, c, d):
  seen.clear()
  makePath(a, b, c, d)
  return len(set((x[0],x[1]) for x in seen))

energies = []

for i in range(len(lines)):
  energies.append(getEnergy(i, 0, 0, 1))
  energies.append(getEnergy(i, len(lines)-1, 0, -1))

for i in range(len(lines[0])):
  energies.append(getEnergy(0, i, 1, 0))
  energies.append(getEnergy(len(lines)-1, i, -1, 0))

print(max(energies))