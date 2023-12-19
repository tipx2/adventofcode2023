with open("day19/input19.txt") as f:
		lines = f.read()

workflows, parts = lines.split("\n\n")

workflows = {x.strip("}").split("{")[0]: x.strip("}").split("{")[1].split(",") for x in workflows.split("\n")}
parts = [{y.split("=")[0]: int(y.split("=")[1]) for y in x.strip("\{\}").split(",")} for x in parts.split("\n")]

def decodeInstruction(inst, part):    
		inst = inst.split(":")[0]

		if "<" in inst:
				var, value = inst.split("<")
				return part[var] < int(value)

		elif ">" in inst:
				var, value = inst.split(">")
				return part[var] > int(value)

		else:
				print("error, > < not in " + inst)


total = 0
for part in parts:
		curr_key = "in"
		while not (curr_key == "A" or curr_key == "R"):
				curr_flow = workflows[curr_key]

				# print(part, curr_key)

				for inst in curr_flow:
						if ":" not in inst:
								curr_key = inst
								break # technically shouldn't need this as the "else" bit is always at the end
						if decodeInstruction(inst, part):
								curr_key = inst.split(":")[1]
								break

		if curr_key == "A":
				total += sum(part.values())

print(total)