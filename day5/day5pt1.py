with open("day5/input5.txt") as f:
    lines = f.read()

lines = [x.split("\n") for x in lines.split("\n\n")]
seeds = [int(x) for x in lines[0][0].split(":")[1].strip().split(" ")]

translations = []
for i in range(1, len(lines)):
    translation = []
    for line in lines[i][1:]:
        t = [int(x) for x in line.split(" ")]
        translation.append(t)
    translations.append(translation)
       
locations = []
for seed in seeds:
    currvalue = seed
    # if source + length > currvalue -1 then it's in range
    for translation in translations:
        for t in translation:
            if t[1] <= currvalue and t[1] + t[2] > currvalue:
                currvalue = t[0] + abs(currvalue - t[1])
                break
    locations.append(currvalue)
print(min(locations))