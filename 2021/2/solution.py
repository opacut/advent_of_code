f = open("2/input.txt", "r")
lines = [l for l in f.read().split("\n")]
for line in lines:
    print(line)
print(lines)

horizontal_position = 0
depth = 0
aim = 0

for line in lines:
    if line.split(" ")[0] == "forward":
        horizontal_position += int(line.split(" ")[1])
        depth += aim*int(line.split(" ")[1])
    elif line.split(" ")[0] == "down":
        #depth += int(line.split(" ")[1])
        aim += int(line.split(" ")[1])
    elif line.split(" ")[0] == "up":
        #depth -= int(line.split(" ")[1])
        aim -= int(line.split(" ")[1])

print("The horizontal position is "+str(horizontal_position)+" and the depth is "+str(depth)+".")
print("Multiplying these gives "+str(horizontal_position*depth))
