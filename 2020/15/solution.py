import os
import pdb
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

def get_last_usage_index(value, turns_dict):
    #iterlist = turns_dict.items()
    indices = [index+1 for index,val in turns_dict.items() if val==value and index < len(list(turns_dict.values()))-1]
    return max(indices) if len(indices)>0 else None

turns = dict()
turns_raw = [int(i) for i in lines[0].split(',')]
for index, turn in enumerate(turns_raw):
    turns[index]=turn
for k,v in turns.items():
    print(f"{k}: {v}")
print(f"{turns}")
#print(f"3 was last used on turn {get_last_usage_index(value=3,turns_dict=turns)}")

turn_number = 1
initial_turns = copy.deepcopy(turns)
last_number = initial_turns[0]
#while turn_number < 2020:
while turn_number < 30000000:
    #print(f"Turn {turn_number} reacts to {last_number}")
    last_number = turns[turn_number-1]
    #print(f"Turn {turn_number+1} reacts to {last_number}")
    if turn_number <= len(initial_turns.keys())-1:
        next_number = initial_turns[turn_number]
    elif last_number not in list(turns.values())[:-1]:
        next_number = 0
    else:
        #pdb.set_trace()
        prev_index = turn_number
        #pdb.set_trace()
        prev_prev_index = get_last_usage_index(value=last_number, turns_dict=turns)
        #pdb.set_trace()
        next_number = prev_index-prev_prev_index
        #pdb.set_trace()
    last_number = next_number
    turns[turn_number] = last_number
    turn_number += 1
    #print(turns)
    print(f"On turn {turn_number}, elf says {next_number}")
    