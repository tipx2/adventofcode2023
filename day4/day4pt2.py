with open("day4/input4.txt") as f:
  lines = f.readlines()


def countWins(l):
  winning, selection = l.split(":")[1].split("|")
  winning = [int(x.strip()) for x in winning.split(" ") if x != ""]
  selection = [int(x.strip()) for x in selection.split(" ") if x != ""]
  total = 0
  for w in winning:
    if w in selection:
      total += 1
  return total


wins = [1 for x in lines]

for x in range(len(lines)):
  # go through the next n and add 1 to each
  for z in range(1, countWins(lines[x]) + 1):
    wins[x + z] += wins[x]

print(sum(wins))