f = open("1/input.txt", "r")
lines = [int(l) for l in f.read().split("\n")]
#for line in lines:
#    print(line)
#print(lines)
inc_count = 0

windows = []
for i in range(0, len(lines)-2):
    windows.append(lines[i]+lines[i+1]+lines[i+2])

for i in range(1, len(windows)):
    diff = "no change"
    if windows[i] < windows[i-1]:
        diff = "decreased"
    elif windows[i] > windows[i-1]:
        inc_count += 1
        diff = "increased"
    print(str(windows[i])+" ("+diff+")")
print("There are "+str(inc_count)+" measurements that are larger than the previous measurement.")