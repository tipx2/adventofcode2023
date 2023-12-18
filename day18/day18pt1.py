with open("day18/input18.txt") as f:
		lines = f.readlines()

outline_arr = [(0,0)]

def debugDraw():
		for x in range(-300, 30):
				for y in range(-250, 250):
						if (x, y) == (0,0):
								print("\033[42m@\033[40m", end="")
						elif (x, y) in outline_arr:
								print("#", end="")
						else:
								print(".", end="")
				print()

for line in lines:
		direction, distance, colour = line.split(" ")
		distance = int(distance)

		if direction == "U":
				direction_vector = (-1, 0)
		elif direction == "D":
				direction_vector = (1, 0)
		elif direction == "R":
				direction_vector = (0, 1)
		elif direction == "L":
				direction_vector = (0, -1)
		else:
				print("invalid direction:", direction)

		currentcoord = outline_arr[-1]
		for i in range(distance + 1):
				outline_arr.append((currentcoord[0] + i*direction_vector[0], currentcoord[1] + i*direction_vector[1]))

outline_arr = set(outline_arr)
#debugDraw()

# flood fill
internal_coords = [(0, 1)] # hardcoded start pos
used = set()

while len(internal_coords) > 0:
		currentcoord = internal_coords.pop()
		used.add(currentcoord)

		for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				new_coord = (currentcoord[0] + d[0], currentcoord[1] + d[1])
				if new_coord in used or new_coord in outline_arr:
						continue
				else:
						internal_coords.append(new_coord)

print(len(used) + len(outline_arr))