from dataclasses import dataclass
with open("day20/input20.txt") as f:
		lines = f.readlines()

HIGH = 1
LOW = 0

modules = {}
pulseQueue = []

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
				self.inputMemory[sender] = p
				if all([x == HIGH for x in self.inputMemory.values()]):
						self.sendPulse(LOW)
				else:
						self.sendPulse(HIGH)

class OutputModule(Module):
		def receivePulse(self, p, sender):
				pass

pulsesCount = [0,0]
def pressButton():
		modules["broadcaster"].receivePulse(LOW, "button")
		while len(pulseQueue) > 0:
				pulse = pulseQueue.pop(0)
				pulsesCount[pulse[1]] += 1
				modules[pulse[0]].receivePulse(pulse[1], pulse[2])
				if pulse[2] != "output":
						pulsetype = "high" if pulse[1] else "low"
						print(pulse[2], "-" + pulsetype + "->", pulse[0])    
		print()


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
		if modules[key].module_type == "&":
				modules[key].initialiseMemory()

button_presses = 1000
pulsesCount[LOW] += button_presses

for _ in range(button_presses):
		pressButton()

print(pulsesCount[LOW], pulsesCount[HIGH])
print(pulsesCount[LOW] * pulsesCount[HIGH])