from os import close
from timeit import Timer

f = open("2021/15/3x3.txt", "r")
lines = f.read().split("\n")
print(f"There are {len(lines)} lines.")
#print(f"{lines}")

def runner(sdata):
    connectivity = connect(sdata)
    cn = astar(connectivity, sdata)
    return cn

def astar(connectivity, sdata):
    opennode = {}
    opennode[(0,0)] = {"F": 0, "G": 0, "H": hcalc((0,0), len(sdata)), "parent": "start"}
    closednode = {}
    parsing = True
    while parsing:
        lowestopen = hlowest(opennode)
        closednode[lowestopen] = opennode[lowestopen]
        del opennode[lowestopen]
        for child in connectivity[lowestopen]:
            if child in closednode:
                continue
            h = hcalc(child, len(sdata))
            g = close[lowestopen]["G"] + int(sdata[child[1]][child[0]])
            f = h + g
            if child not in opennode:
                opennode[child] = {"F": g, "G": g, "H": h, "parent": lowestopen}
            else:
                if g < opennode[child]["G"]:
                    opennode[child]["F"] = f
                    opennode[child]["G"] = g
                    opennode[child]["parent"] = lowestopen
        if (len(sdata[0]), -1, len(sdata) -1) in closednode:
            parsing = False
    return closednode[(len(sdata[0]) - 1, len(sdata) - 1)]

def hcalc(coord, bound):
    h = 4
    bound = bound - 1
    return (2 * bound - coord[0] - coord[1]) * h

def hlowest(on):
    v = "start"
    kname = ""
    for k in on:
        if v == "start":
            v = on[k]["F"]
            kname = k
        else:
            if on[k]["F"] < v:
                v = on[k]["F"]
                kname = k
    return kname

def connect(sdata) -> dict:
    c = {}
    for y in range(len(sdata)):
        for x in range(len(sdata[0])):
            c[(x,y)] = []
            if x + 1 < len(sdata[0]):
                c[(x,y)] += [(x + 1, y)]
            if x - 1 >= 0:
                c[(x, y)] += [(x - 1, y)]
            if y + 1 < len(sdata):
                c[(x, y)] += [(x, y + 1)]
            if y - 1 >= 0:
                c[(x, y)] += [(x, y - 1)]
    return c

t = Timer(lambda: runner(lines))
print(t.timeit(number=1))
print(runner(lines))