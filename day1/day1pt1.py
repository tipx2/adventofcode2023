with open("day1/input1.txt") as f:
  lines = f.readlines()

total = 0
for line in lines:
  line = [x for x in line.strip() if x.isdigit()]
  line = line[0] + line[-1]
  total += int(line)

print(total)
