# solution from hyperneutrino, adapted a little bit
from heapq import heappop, heappush
with open("day17/input17.txt") as f:
  lines = [[int(x) for x in y] for y in f.read().strip().split("\n")]

bottom_right_coord = (len(lines)-1, len(lines[0])-1)

used = set()
priority_q = [(0, (0,0),(0,0),0)] # current coordinate, direction, weight, number of coords in a row

while priority_q:
  current_weight, current_coord, current_direction, current_n_in_row = heappop(priority_q)
  
  #print(current_weight)
  if current_coord == bottom_right_coord and current_n_in_row >= 4:
    print(current_weight)
    break
  
  if (current_coord, current_direction, current_n_in_row) in used: # excluding weight, to avoid loops
    continue
  
  used.add((current_coord, current_direction, current_n_in_row))
  
  # if it's not the first tile and we are allowed to go in a straight line
  if current_n_in_row < 10 and current_direction != (0, 0): 
    # keep going in the same direction
    new_coord = (current_coord[0] + current_direction[0], current_coord[1] + current_direction[1])
    
    # boundary check the new coordinate
    if 0 <= new_coord[0] < len(lines) and 0 <= new_coord[1] < len(lines[0]):
      heappush(priority_q, (current_weight + lines[new_coord[0]][new_coord[1]], new_coord, current_direction, current_n_in_row + 1))
  
  if current_n_in_row >= 4 or current_direction == (0,0):
    # if we need to turn
    for new_direction in [(0,1), (1, 0), (0, -1), (-1, 0)]:
      # make sure we aren't going in the same direction (accounted for earlier) or back on ourselves
      if new_direction != current_direction and new_direction != (-current_direction[0], -current_direction[1]): 
        new_coord = (current_coord[0] + new_direction[0], current_coord[1] + new_direction[1])
        if 0 <= new_coord[0] < len(lines) and 0 <= new_coord[1] < len(lines[0]):
          heappush(priority_q, (current_weight + lines[new_coord[0]][new_coord[1]], new_coord, new_direction, 1))