import re
with open("day1/input1.txt") as f:
  lines = f.readlines()

numberdict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def numberT(s):
  if s.isdigit():
    return s
  else:
    return numberdict[s]

total = 0
for line in lines:
  matches = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
  
  number = int(numberT(line[0]) + numberT(line[-1]))
  total += number

print(total)
