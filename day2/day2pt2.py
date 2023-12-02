with open("day2/input2.txt") as f:
  lines = f.readlines()


def findPower(l):
  red = 0
  green = 0
  blue = 0
  for group in l:
    for pull in group:
      pull = pull.strip()
      num, colour = pull.split(" ")
      num = int(num)
      if colour == "red" and num > red:
        red = num
      elif colour == "blue" and num > blue:
        blue = num
      elif colour == "green" and num > green:
        green = num
  
  return red * green * blue
  
total = 0
for line in lines:
  lineid, line = line.split(":")
  lineid = int(lineid[5:])
  
  line = [x.strip().split(",") for x in line.split(";")]
  
  total += findPower(line)

print(total)