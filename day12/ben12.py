from functools import cache
import time
@cache
def recursion(parts,groups,currentGroupLength):
    temp = 0

    #print(parts,groups,currentGroupLength)
    if parts == "":
        if groups == () and currentGroupLength == 0:
            #print("good")
            pass
        elif groups == (currentGroupLength,):
            #print("good")
            pass
        else:
            #print("bad")
            return 0
        return 1
    if parts[0] == "?":
        temp += recursion("#"+parts[1:],groups,currentGroupLength)
        temp += recursion("."+parts[1:],groups,currentGroupLength)        
    elif parts[0] == ".":
        if currentGroupLength > 0:
            if currentGroupLength != groups[0]:
                #print("bad")
                return 0
            else:
                temp += recursion(parts[1:],groups[1:],0) #end of a group
        else:
            temp += recursion(parts[1:],groups,0)
    elif parts[0] == "#":
        if groups == ():
            #print("bad")
            return 0
        currentGroupLength += 1
        if currentGroupLength > groups[0]:
            #print("bad")
            return 0
        else:
            temp += recursion(parts[1:],groups,currentGroupLength)
    return temp

with open("day12/test12.txt") as f:
    data = [[x.split(" ")[0],[int(y) for y in x.split(" ")[1].split(",")]] for x in f.read().split("\n")]
# #print(data)
total = 0
# data = [["?????????????#????", [1, 1, 10]]]
s = time.time()

for parts, groups in data:
    p = parts+"?"+parts+"?"+parts+"?"+parts+"?"+parts
    g = 5*groups
    total += recursion(p,tuple(g),0)
print(total)
# exit()
print(time.time() - s)