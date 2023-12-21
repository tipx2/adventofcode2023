with open("day19/input19.txt") as f:
		lines = f.read()

workflows, parts = lines.split("\n\n")

workflows = {x.strip("}").split("{")[0]: x.strip("}").split("{")[1].split(",") for x in workflows.split("\n")}
paths = []

def conditionFlipper(cond):
		if ">" in cond:
				return cond.replace(">", "<=")
		elif "<" in cond:
				return cond.replace("<", ">=")


def findPath(conditions, path, target):
		path = path + (target,)

		if target == "A" or target == "R": # base case
				paths.append((path, conditions))
				return

		curr_flow = workflows[target]
		curr_flow, elserule = curr_flow[:-1], curr_flow[-1]

		elseconds = ()

		for instruction in curr_flow:
				condition, new_target = instruction.split(":")
				findPath(conditions + elseconds + (condition,), path, new_target)
				elseconds = elseconds + (conditionFlipper(condition),)

		findPath(conditions + elseconds, path, elserule)

def processRange(ra):
		total = 1
		for x in "xmas":
				total *= (ra[x][1] - ra[x][0] + 1)
		return total

findPath((), (), "in")
paths = [x for x in paths if x[0][-1] == "A"]

allranges = []
for path in paths:
		startranges = {"x": [1, 4000], "m": [1, 4000],"a": [1, 4000],"s": [1, 4000]}
		conditions = path[1]
		for cond in conditions:
				if "<=" in cond:
						var, value = cond.split("<=")
						startranges[var][1] = min(startranges[var][1], int(value))
				elif "<" in cond:
						var, value = cond.split("<")
						startranges[var][1] = min(startranges[var][1], int(value)-1)

				if ">=" in cond:
						var, value = cond.split(">=")
						startranges[var][0] = max(startranges[var][0], int(value))
				elif ">" in cond:
						var, value = cond.split(">")
						startranges[var][0] = max(startranges[var][0], int(value)+1)

		allranges.append(startranges)


print(sum([processRange(r) for r in allranges]))