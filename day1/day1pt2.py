import re
with open("day1/input1.txt") as f:
  lines = f.readlines()

def numberT(s):
  if s.isdigit():
    return s
  elif s == "one":
    return "1"
  elif s == "two":
    return "2"
  elif s == "three":
    return "3"
  elif s == "four":
    return "4"
  elif s == "five":
    return "5"
  elif s == "six":
    return "6"
  elif s == "seven":
    return "7"
  elif s == "eight":
    return "8"
  elif s == "nine":
    return "9"

total = 0
for line in lines:
  line = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
  print(line)
  
  
  line = numberT(line[0]) + numberT(line[-1])
  print(line)
  total += int(line)

print(total)
