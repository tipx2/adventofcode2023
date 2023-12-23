with open("day23/input23.txt") as f:
  lines = [x.strip() for x in f.readlines()]

def debugDraw(used, curr_node):
  for x in range(len(lines)):
    for y in range(len(lines[0])):
      if (x, y) in used:
        print("O", end="")
      elif (x, y) == curr_node:
        print("X", end="")
      else:
        print(lines[x][y], end="")
    print()

pathqueue = [(set(), (0, lines[0].index(".")))]
target = (len(lines)-1, lines[len(lines)-1].index("."))

finished = []

while len(pathqueue) > 0:
  visited, curr_node = pathqueue.pop()
  curr_tile = lines[curr_node[0]][curr_node[1]]
  
  
  if curr_node in visited:
    continue
  elif curr_node == target:
    finished.append(len(visited))
    continue

  
  visited.add(curr_node)
  
  if curr_tile in "><^v":
    
    if curr_tile == ">":
      new_row = curr_node[0]
      new_col = curr_node[1] + 1
    elif curr_tile == "<":
      new_row = curr_node[0]
      new_col = curr_node[1] - 1
    elif curr_tile == "v":
      new_row = curr_node[0] + 1
      new_col = curr_node[1]
    elif curr_tile == "^":
      new_row = curr_node[0] - 1
      new_col = curr_node[1]
    
    if not (0 <= new_row < len(lines) and 0 <= new_col < len(lines[0])):
      continue

    new_tile = lines[new_row][new_col]
    
    if new_tile == "#" or (new_row, new_col) in visited:
      continue
    else:
      pathqueue.append((visited.copy(), (new_row, new_col)))
      
  elif curr_tile == ".":
    for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      new_row = curr_node[0] + direction[0]
      new_col =  curr_node[1] + direction[1]
      
      if not (0 <= new_row < len(lines) and 0 <= new_col < len(lines[0])):
        continue

      new_tile = lines[new_row][new_col]
      
      if new_tile == "#" or (new_row, new_col) in visited:
        continue
      else:
        pathqueue.append((visited.copy(), (new_row, new_col)))

print(max(finished))