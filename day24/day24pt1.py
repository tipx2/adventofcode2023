with open("day24/input24.txt") as f:
  lines = [x.strip() for x in f.readlines()]

hail = []

low, high = 200000000000000, 400000000000000
# low, high = 7, 27

for line in lines:
  pos, vel = [[int(x) for x in y.split(", ")] for y in line.split(" @ ")]
  
  gradient = vel[1] / vel[0] # change in y over change in x
  c_term = vel[1] + pos[1] - gradient * (vel[0] + pos[0]) # y-y_1 = m(x-x_1) and rearrange for c term
  hail.append((gradient, c_term, pos[0], pos[1], vel[0], vel[1]))



total = 0
for i in range(len(hail)):
  hailstone1 = hail[i]
  for j in range(i+1, len(hail)):
    hailstone2 = hail[j]
    
    if hailstone1[2] == 0 or hailstone1[3] == 0 or hailstone2[2] == 0 or hailstone2[3] == 0:
      print(i, j, x, y)
    
    if hailstone1[0] == hailstone2[0]: # parallel, ignore
      continue
    
    x = (hailstone2[1] - hailstone1[1]) / (hailstone1[0] - hailstone2[0])
    y = hailstone1[0] * x + hailstone1[1]
    
    
    if x > hailstone1[2] and hailstone1[4] < 0: # if x has increased and the x velocity is negative
      continue
    if y > hailstone1[3] and hailstone1[5] < 0: # if y has increased and the y velocity is negative
      continue
    
    if x < hailstone1[2] and hailstone1[4] > 0: # if x has increased and the x velocity is negative
      continue
    if y < hailstone1[3] and hailstone1[5] > 0: # if y has increased and the y velocity is negative
      continue
    
    if x > hailstone2[2] and hailstone2[4] < 0: # you figure it out
      continue
    if y > hailstone2[3] and hailstone2[5] < 0:
      continue
    
    if x < hailstone2[2] and hailstone2[4] > 0:
      continue
    if y < hailstone2[3] and hailstone2[5] > 0:
      continue
    
    if low <= x <= high and low <= y <= high:
      
      total += 1

print(total)