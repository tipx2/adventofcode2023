import re
with open("day12/input12.txt") as f:
    lines = f.readlines()

def checkLineGrouping(s : str, g : list):
    matches = [len(x) for x in re.findall("#+", s)]
    return matches == g


total = 0
for z, line in enumerate(lines):
    if z % 100 == 0:
        print("av", z)
    springs, grouping = line.split(" ")
    grouping = [int(x.strip()) for x in grouping.split(",")]

    configs = 0
    qmarks_count = springs.count("?")
    for i in range(2**qmarks_count):
        # do the nth combination thing here
        currbinary = format(i, "b").zfill(qmarks_count).replace("1", "#").replace("0", ".")
        
        if sum(grouping) != springs.count("#") + currbinary.count("#"):
          continue

        cbpointer = 0
        check_springs = ""
        for chara in springs:
            if chara != "?":
                check_springs += chara
            else:
                check_springs += currbinary[cbpointer]
                cbpointer += 1

        if checkLineGrouping(check_springs, grouping):
            configs += 1
    total += configs

print(total)