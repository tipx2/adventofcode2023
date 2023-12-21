from dataclasses import dataclass
from math import gcd
with open("day20/input20.txt") as f:
		lines = f.readlines()

HIGH = 1
LOW = 0

modules = {}
pulseQueue = []
press_count = 0

pointing_to_bb = []
cycles = {}

@dataclass
class Module:
		module_name : str
		module_type : str
		inputs : list
		outputs : list

		def receivePulse(self, p, sender):
				self.sendPulse(p) # for broadcaster - default behaviour

		def sendPulse(self, p):
				for output in self.outputs:
						pulseQueue.append((output, p, self.module_name))


class FlipFlop(Module):
		isOn : bool = False

		def receivePulse(self, p, sender):
				if p == LOW:
						if self.isOn:
								self.sendPulse(LOW)
						else:
								self.sendPulse(HIGH)
						self.isOn = not self.isOn

class Conjunction(Module):
		inputMemory : dict

		def initialiseMemory(self):
				self.inputMemory = {x: LOW for x in self.inputs}

		def receivePulse(self, p, sender):
				if p == LOW and self.module_name in pointing_to_bb:
						cycles[self.module_name] = press_count
				self.inputMemory[sender] = p
				if all([x == HIGH for x in self.inputMemory.values()]):
						self.sendPulse(LOW)
				else:
						self.sendPulse(HIGH)


class OutputModule(Module):
		def receivePulse(self, p, sender):
				pass

def pressButton():
		modules["broadcaster"].receivePulse(LOW, "button")
		while len(pulseQueue) > 0:
				pulse = pulseQueue.pop(0)
				modules[pulse[0]].receivePulse(pulse[1], pulse[2])


for line in lines:
		name, outputs = line.split(" -> ")
		outputs = [x.strip() for x in outputs.split(",")]
		if name == "broadcaster":
				mod_type = "broadcaster"
		else:
				mod_type, name = name[0], name[1:]

		if mod_type == "%":
				modules[name] = FlipFlop(name, mod_type, [], outputs)
		elif mod_type == "&":
				modules[name] = Conjunction(name, mod_type, [], outputs)
		else:
				modules[name] = Module(name, mod_type, [], outputs) # should only run for broadcaster and rx

modules["rx"] = OutputModule("rx", "rx", [], [])
# modules["output"] = OutputModule("rx", "rx", [], [])

for key in modules.keys():
		for output in modules[key].outputs:
				modules[output].inputs.append(key)

for key in modules.keys():
		if modules[key].module_type == "&":
				modules[key].initialiseMemory()


pointing_to_rx = modules["rx"].inputs[0]

# in my input, bb points to rx. 4 conjunctions point to bb
pointing_to_bb = modules[pointing_to_rx].inputs

cycles = {mod: 0 for mod in pointing_to_bb}

while True:
		press_count += 1
		pressButton()

		if 0 not in cycles.values():
				break

total = 1
for item in cycles.values():
		total = total * item // gcd(total, item)

print(cycles.values())
print(total)