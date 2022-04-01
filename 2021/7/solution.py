import pdb
f = open("7/input.txt", "r")
lines = [int(x) for x in f.read().split(",")]
#print(lines)

max_position = max(lines)
print(f"Max position is {max_position}")

fuel_costs = []
for pos in range(max_position):
    print(f"Processing position {pos} of {max_position}")
    total_fuel = 0
    for crab in lines:
        #total_fuel += abs(crab - pos)
        for i in range(abs(crab - pos)):
            total_fuel += abs(crab - pos)-i
    fuel_costs.append(total_fuel)
print(f"Fuel costs {fuel_costs}")
min_fuel_index = 0
for i in range(len(fuel_costs)):
    if fuel_costs[i] < fuel_costs[min_fuel_index]:
        min_fuel_index = i
print(f"The crabs should align at position {min_fuel_index} and it will cost {fuel_costs[min_fuel_index]} fuel.")
