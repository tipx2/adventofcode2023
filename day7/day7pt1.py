from collections import Counter
from itertools import chain

with open("day7/input7.txt") as f:
  lines = f.readlines()


biddicts = {x.split(" ")[0]: int(x.split(" ")[1]) for x in lines}
hands = biddicts.keys()

handranks = [[], [], [], [], [], [], []] # fivekind, fourkind, full house, threekind, twopair, onepair, highcard

cardRanks = {"A":13, "K":12, "Q":11, "J":10, "T":9, "9":8, "8":7, "7":6, "6":5, "5":4, "4":3, "3":2, "2":1}

def rankIsLessThan(hand1, hand2): # return true if hand1 is less than hand2
  for x in range(5):
    if hand1[x] == hand2[x]:
      continue
    else:
      return cardRanks[hand1[x]] < cardRanks[hand2[x]]

def bubblesort(r):
  n = len(r)
  for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
      if rankIsLessThan(r[j], r[j + 1]):
        swapped = True
        r[j], r[j + 1] = r[j + 1], r[j]
    if not swapped:
      return


for hand in hands:
  cardCount = Counter(hand)
  counts = list(cardCount.values())
  if 5 in counts:
    handranks[0].append(hand)
  elif 4 in counts:
    handranks[1].append(hand)
  elif 3 in counts and 2 in counts:
    handranks[2].append(hand)
  elif 3 in counts:
    handranks[3].append(hand)
  elif counts.count(2) == 2:
    handranks[4].append(hand)
  elif 2 in counts:
    handranks[5].append(hand)
  else:
    handranks[6].append(hand)

# print(handranks)

for r in handranks:
  if len(r) == 1:
    continue
  else:
    bubblesort(r)


handranks = list(chain.from_iterable(handranks))

total = 0
for i, hand in enumerate(reversed(handranks)):
  total += (i + 1) * biddicts[hand]

print(total)