with open("day6/input6.txt") as f:
  lines = f.readlines()

time = int(lines[0].split(":")[1].strip().replace(" ", ""))
distance = int(lines[1].split(":")[1].strip().replace(" ", ""))


# test input
# time = 71530
# distance = 940200

beaten_ways = 0
for x in range(time):
  if x % 10000 == 0:
    print("AV", x)
  timedist = (time - x) * x
  if timedist > distance:
    beaten_ways += 1

print(beaten_ways)