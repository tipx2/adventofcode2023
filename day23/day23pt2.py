import sys
sys.setrecursionlimit(4_294_967)
# warning: incredibly slow

with open("day23/input23.txt") as f:
  lines = [x.strip() for x in f.readlines()]

# find all intersections
# find connections between all intersections, with weights
# dfs resulting graph

lines = [line.translate(str.maketrans({">": ".", "^": ".", "v": ".", "<": "."})) for line in lines]


intersections = []

# find all intersections
for i, line in enumerate(lines):
  for j, letter in enumerate(line):
    if letter == ".":
      num_dirs = [False, False, False, False]
      for n, direction in enumerate([(i-1, j), (i+1, j), (i, j-1), (i, j+1)]):
        if not (0 <= direction[0] < len(lines) and 0 <= direction[1] < len(lines[0])):
          continue
        if lines[direction[0]][direction[1]] == ".":
          num_dirs[n] = True
      
      if num_dirs.count(True) == 2:
        if num_dirs != [False, False, True, True] and num_dirs != [True, True, False, False]:
          intersections.append((i, j))
      elif num_dirs.count(True) > 0:
        intersections.append((i, j))

# find connections between all intersections, with weights
def reachOut(startpos, direction):
  curr_block = (startpos[0] + direction[0], startpos[1] + direction[1])
  while True:
    if not (0 <= curr_block[0] < len(lines) and 0 <= curr_block[1] < len(lines[0])):
      return False, startpos
    if lines[curr_block[0]][curr_block[1]] == "#":
      return False, startpos
    if curr_block in intersections:
      return True, curr_block
    else:
      curr_block = (curr_block[0] + direction[0], curr_block[1] + direction[1])

graph = {}
for intersection in intersections:
  for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    found, pos = reachOut(intersection, direction)
    if found:
      weight = abs(pos[0] - intersection[0]) + abs(pos[1] - intersection[1])
      if intersection in graph:
        graph[intersection].append((weight, pos))
      else:
        graph[intersection] = [(weight, pos)]

# dfs resulting graph
pathqueue = [(0, (0, lines[0].index(".")))]
target = (len(lines)-1, lines[len(lines)-1].index("."))

visited = set()
finished = []

def backtrack(weight, curr_pos, counter=0):
  global finished
  
  if curr_pos in visited:
    return
  elif curr_pos == target:
    finished.append(weight)
    return

  visited.add(curr_pos)
  
  for neighbor in graph[curr_pos]:
    nweight, npos = neighbor
    
    backtrack(nweight + weight, npos)

  visited.remove(curr_pos)

backtrack(0, (0, lines[0].index(".")))
print(finished)
print(max(finished))