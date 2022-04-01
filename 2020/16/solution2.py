import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
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
        self.actual_index = None
        self.actual_indices = list()

    def __str__(self):
        return f"{self.name}: {self.interval_one} or {self.interval_two}, actual index is {self.actual_indices}"

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

#print(f"fields: {[field.__str__() for field in fields]}") 
#print(f"my ticket: {my_ticket}")
#print(f"tickets: {tickets}")

invalid_tickets = list()
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
            invalid_tickets.append(ticket)
            break

columns = list()
#columns = [[]]*len(tickets[0])
for i in range(len(tickets[0])):
    columns.append([])
#pdb.set_trace()
for ticket in tickets:
    if ticket in invalid_tickets:
        continue
    for i,v in enumerate(ticket):
        #pdb.set_trace()
        columns[i].append(v)

for column_index, column in enumerate(columns):
    for field in fields:
        if all([field.is_valid(value=v) for v in column]) and field.actual_index == None:
        #if field.is_valid(column):
            #field.actual_index = column_index
            field.actual_indices.append(column_index)
            #break


#print(f"Invalid numbers: {invalid_numbers}")
#print(f"Ticket error scanning rate: {sum(invalid_numbers)}")
#print(f"Invalid tickets: {invalid_tickets}")
#print(f"columns: {columns}")
f = [(field.name, field.actual_indices) for field in fields]
print(f"fields are: {f}")
#pdb.set_trace()
print(my_ticket[14]*my_ticket[0]*my_ticket[12]*my_ticket[6]*my_ticket[19]*my_ticket[18])
#14 0 12 6 19 18