import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
bags = dict()
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")
    for line in lines:
        if line != '':
            split_one = line.split(" bags contain ")
            name = split_one[0]
            rules_split = split_one[1].split(", ")
            bag_rules = dict()
            for rule in rules_split:
                rule_split = rule.split(" ")
                if rule_split[0] == "no":
                    bag_rules = dict()
                else:
                    rule_name = rule_split[1]+" "+rule_split[2]
                    bag_rules[rule_name] = int(rule_split[0])
            bags[name] = bag_rules

def can_be_in(bags, search_name):
    can_be_in = list()
    for bag_name, bag_rules in bags.items():
        for rule_name, rule_value in bag_rules.items():
            if rule_name == search_name:
                can_be_in.append(bag_name)
                continue
    return can_be_in

def process_bags(bags, search_name, function):
    final_function_result = list()
    previous_function_result = function(bags=bags, search_name=search_name)
    for c in previous_function_result:
        if c not in final_function_result:
            final_function_result.append(c)

    while len(previous_function_result) > 0:
        new_function_result = [item for sublist in [function(bags=bags, search_name=y) for y in previous_function_result] for item in sublist]
        for c in new_function_result:
            if c not in final_function_result:
                final_function_result.append(c)
        previous_function_result = new_function_result

    return final_function_result

def process(bags, search_name):
    total_bags_needed = -1
    bags_to_process = [search_name]
    while len(bags_to_process) > 0:
        bag = bags_to_process.pop(0)
        total_bags_needed += 1
        if len(bags[bag]) == 0:
            continue
        for bag, count in bags[bag].items():
            for i in range(count):
                bags_to_process.append(bag)
    return total_bags_needed

print(process(bags=bags, search_name="shiny gold"))