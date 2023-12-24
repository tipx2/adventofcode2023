from z3 import *
with open("day24/input24.txt") as f:
  lines = [x.strip() for x in f.readlines()]

solver = Solver()
x, y, z = Ints("x y z")
dx, dy, dz = Ints("dx dy dz")

for i, line in enumerate(lines):
  pos, vel = [[int(x) for x in y.split(", ")] for y in line.split(" @ ")]
  
  t = Int("t" + str(i))
  
  # maths comes in here
  solver.add(x + dx * t == pos[0] + vel[0] * t)
  solver.add(y + dy * t == pos[1] + vel[1] * t)
  solver.add(z + dz * t == pos[2] + vel[2] * t)

solver.check()
m = solver.model()

print(m[x].as_long() + m[y].as_long() + m[z].as_long())