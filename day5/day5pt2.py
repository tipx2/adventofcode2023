with open("day5/input5.txt") as f:
  lines = f.read()

lines = [x.split("\n") for x in lines.split("\n\n")]
seeds = [int(x) for x in lines[0][0].split(":")[1].strip().split(" ")]

def checkIfSeed(n):
  for i in range(0, len(seeds), 2):
    if seeds[i] <= n and seeds[i] + seeds[i + 1] > n:
      return True
  return False

translations = []
for i in range(1, len(lines)):
  translation = []
  for line in lines[i][1:]:
    t = [int(x) for x in line.split(" ")]
    translation.append(t)
  translations.append(translation)

for x in range(100000000000):
    if x % 1000000 == 0:
        print("AV", x)
    currvalue = x
    for translation in translations[::-1]:
        for t in translation:
            if t[0] <= currvalue and t[0] + t[2] > currvalue:
                currvalue = t[1] + abs(currvalue - t[0])
                break
    if checkIfSeed(currvalue):
      print(x)
      break