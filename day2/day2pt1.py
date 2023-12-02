with open("day2/input2.txt") as f:
  lines = f.readlines()

# red 12, green 13, blue 14
def sumline(l):
  for group in l:
    for pull in group:
      pull = pull.strip()
      num, colour = pull.split(" ")
      num = int(num)
      if (colour == "red" and num > 12) or (colour == "green" and num > 13) or (colour == "blue" and num > 14):
        return False
  return True

total = 0
for line in lines:
  lineid, line = line.split(":")
  lineid = int(lineid[5:])
  
  line = [x.strip().split(",") for x in line.split(";")]
  
  if sumline(line):
    total += lineid

print(total)