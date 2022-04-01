import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'proof.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

class Interval:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def validate(self, value):
        return value >= self.start and value <= self.stop
    
    def __str__(self):
        return f"{self.start}-{self.stop}"

class Field:
    def __init__(self, init_string):
        self.name = init_string.split(": ")[0]
        #pdb.set_trace()
        interval_one_start = int(init_string.split(": ")[1].split(" ")[0].split("-")[0])
        interval_one_stop = int(init_string.split(": ")[1].split(" ")[0].split("-")[1])
        interval_two_start = int(init_string.split(": ")[1].split(" ")[2].split("-")[0])
        interval_two_stop = int(init_string.split(": ")[1].split(" ")[2].split("-")[1])
        self.interval_one = Interval(start=interval_one_start,stop=interval_one_stop)
        self.interval_two = Interval(start=interval_two_start,stop=interval_two_stop)

    def __str__(self):
        return f"{self.name}: {self.interval_one} or {self.interval_two}"

    def is_valid(self, value):
        return self.interval_one.validate(value=value) or self.interval_two.validate(value=value)



fields = list()
my_ticket = list()
tickets = list()
invalid_tickets = list()
fields_loaded = False
my_ticket_loaded = False
for line in lines:
    #if line == "":
    #    fields_loaded = True
    if not fields_loaded:
        if line == "":
            fields_loaded = True
        else:
            fields.append(Field(init_string=line))
    elif not my_ticket_loaded:
        if line == "your ticket:":
            continue
        if line == "":
            my_ticket_loaded = True
        else:
            my_ticket = [int(v) for v in line.split(",")]
    else:
        if line == "nearby tickets:":
            continue
        if line == "":
            break
        else:
            tickets.append([int(v) for v in line.split(",")])

print(f"fields: {[field.__str__() for field in fields]}") 
print(f"my ticket: {my_ticket}")
print(f"tickets: {tickets}")

invalid_numbers = list()
for ticket in tickets:
    #print(f"Processing ticket {ticket}")
    for n in ticket:
        #print(f"Processing number {n}")
        for field in fields:
            #print(f"Valid for field {field.__str__()}?")
            if field.is_valid(value=n):
                #print(f"Yes.")
                break
            #else:
                #print("No.")
        else:
            #print(f"Adding an invalid number: {n}")
            invalid_numbers.append(n)

print(f"Invalid numbers: {invalid_numbers}")
print(f"Ticket error scanning rate: {sum(invalid_numbers)}")
