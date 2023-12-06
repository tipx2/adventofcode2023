with open("day6/input6.txt") as f:
  lines = f.readlines()

def multiplyAll(l):
  total = 1
  for value in l:
    total *= value
  return total


times = [int(x) for x in lines[0].split(":")[1].strip().split("     ")]
distances = [int(x) for x in lines[1].split(":")[1].strip().split("   ")]

# test input
# times = [7, 15, 30]
# distances = [9, 40, 200]

beating = []
for i in range(len(times)):
  beaten_ways = 0
  for x in range(times[i]):
    timedist = (times[i] - x) * x
    if timedist > distances[i]:
      beaten_ways += 1
  beating.append(beaten_ways)

print(beating)
print(multiplyAll(beating))