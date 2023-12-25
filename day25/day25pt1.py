with open("day25/input25.txt") as f:
  lines = [x.strip() for x in f.readlines()]

connections = {}

for line in lines:
  key, values = line.split(": ")
  values = values.split(" ")
  
  for value in values:
    if value in connections:
      connections[value].append(key)
    else:
      connections[value] = [key]
    
    if key in connections:
      connections[key].append(value)
    else:
      connections[key] = [value]

with open("day25/in.dot", "w") as f:
  store = set()
  for key in connections.keys():
    for value in connections[key]:
      if (key, value) not in store and (value, key) not in store:
        f.write(key + " -> " + value + ";\n")
        store.add((key, value))

# use the above file with graphviz

# VERY HARDCODED BELOW!!
# manually spotted connections from graphviz visualisation of data:
# jct -> rgv
# crg -> krf
# zhg -> fmr

connections["jct"].remove("rgv")
connections["rgv"].remove("jct")

connections["crg"].remove("krf")
connections["krf"].remove("crg")

connections["zhg"].remove("fmr")
connections["fmr"].remove("zhg")

# dfs from rgv and jct
def count_nodes(connections, start_node):
    visited = set()
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack = stack + list(set(connections[node]) - visited)
    
    return len(visited)

rgv = count_nodes(connections, "rgv")

jct = count_nodes(connections, "jct")

print("rgv", rgv)
print("jct", jct)
print(rgv * jct)