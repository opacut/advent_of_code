import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()


earliest_timestamp = int(lines[0])
departing_buses = [int(timestamp) for timestamp in lines[1].split(",") if timestamp != 'x']
print(f"Earliest timestamp: {earliest_timestamp}. Departing buses: {departing_buses}")
remainders = [int(earliest_timestamp)%int(y) for y in departing_buses]
print(f"Which would correspond to {remainders}")

bus_to_take = 0
next_arrivals = dict()
for bus in departing_buses:
    bus_remainder = earliest_timestamp/bus
    next_bus = (bus*(int(earliest_timestamp/bus))+bus)-earliest_timestamp
    next_arrivals[bus] = next_bus
print(f"Next arrivals: {next_arrivals}")

earliest_arriving_time = min(list(next_arrivals.values()))
earliest_bus = None
wait_for = None
for k,v in next_arrivals.items():
    if v == earliest_arriving_time:
        wait_for = v
        earliest_bus = k
print(f"Earliest bus to come is {earliest_bus}. You'll be waiting {wait_for}. Multiplied, that is {earliest_bus*wait_for}")