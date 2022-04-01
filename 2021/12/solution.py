f = open("12/example.txt", "r")
lines = f.read().split("\n")
print(f"There are {len(lines)} lines.")
print(lines)