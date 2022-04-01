from collections import Counter

f = open("2021/14/input.txt", "r")
lines = f.read().split("\n")
print(f"There are {len(lines)} lines.")

initial_polymer = lines[0]
rules = [(x.split(" -> ")[0], x.split(" -> ")[1]) for x in lines[2:]]
print(f"Initial polymer: {initial_polymer}")
print(f"rules: {rules}")
monomer_types = ''.join(set(initial_polymer))

def get_pairs(polymer):
    pairs = []
    for i in range(len(polymer)-1):
        pairs.append(""+polymer[i]+polymer[i+1])
    return pairs

def process_pair(pair):
    for rule in rules:
        if rule[0] == pair:
            return ""+pair[0]+rule[1]


working_polymer = initial_polymer
steps = 40
for i in range(steps):
    print(f"\nProcessing step {i+1}")
    new_polymer = ""
    pairs = get_pairs(polymer=working_polymer)
    for pair in pairs:
        new_polymer += process_pair(pair=pair)
    new_polymer += initial_polymer[-1]
    working_polymer = new_polymer
    print(f"Polymer length after {i+1} steps is {len(working_polymer)}")

final_polymer = working_polymer
#frequency = dict()
#for monomer_type in monomer_types:
#    frequency[monomer_type] = 
ct = Counter(final_polymer)
print(f"Count of all monomers in the final polymer: {str(ct)}")
minimum = int([v for v in list(dict(ct).values()) if v == min(list(dict(ct).values()))][0])
maximum = int([v for v in list(dict(ct).values()) if v == max(list(dict(ct).values()))][0])
print(f"Maximum is {maximum} and minimum is {minimum}")
print(f"Subtracted, it's {maximum - minimum}")