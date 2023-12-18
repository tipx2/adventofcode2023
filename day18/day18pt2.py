with open("day18/input18.txt") as f:
	lines = f.readlines()

outline_arr = [(0,0)]
outline_meters = 0

for line in lines:
	hexcode = line.split("#")[1].strip().strip(")")
	hexcode, direction = hexcode[:-1], hexcode[-1]
	distance = int(hexcode, 16)

	if direction == "3":
			direction_vector = (-1, 0)
	elif direction == "1":
			direction_vector = (1, 0)
	elif direction == "0":
			direction_vector = (0, 1)
	elif direction == "2":
			direction_vector = (0, -1)
	else:
			print("invalid direction:", direction)

	currentcoord = outline_arr[-1]
	endcoord = (currentcoord[0] + distance * direction_vector[0], currentcoord[1] + distance * direction_vector[1])
	outline_arr.append(endcoord)
	outline_meters += distance


# shoelace formula:
# area of polygon = 0.5 * (x_0 * y_1 - x_1 * y_0 + x_2 * y_3 - x_3 - y_2 ...)
area = 0
for i in range(len(outline_arr) - 1):
	x0, y0 = outline_arr[i]
	x1, y1 = outline_arr[i+1]
	area += x0 * y1 - x1 * y0
area = abs(area) // 2

# pick's theorem:
# number of interior points = area of polygon - (number of boundary points/2) + 1
interior_points = area - (outline_meters//2) + 1

print(interior_points + outline_meters)