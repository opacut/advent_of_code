import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
strings = []
with open(os.path.join(__location__, 'input.txt')) as f:
    strings = f.read().split("\n")

nice_strings = []
naughty_strings = []

def contains_three_vowels(s):
    total = 0
    for vowel in "aeiou":
        total += s.lower().count(vowel)
    return total > 2

def contains_duplicate_letter(s):
    index_1 = 0
    index_2 = 1
    while index_2 < len(s):
        if s[index_1].lower() == s[index_2].lower():
            return True
        index_1 += 1
        index_2 += 1
    return False

def contains_no_naughty_substrings(s):
    if ("ab" in s) or ("cd" in s) or ("pq" in s) or ("xy" in s):
        return False
    return True

#def is_nice(s):
#    return contains_three_vowels(s) and contains_duplicate_letter(s) and contains_no_naughty_substrings(s)

def contains_nonoverlapping_pairs(s):
    s = s.lower()
    outer_index_1 = 0
    outer_index_2 = 1
    while(outer_index_2 < len(s)):
        first_pair = [s[outer_index_1], s[outer_index_2]]
        inner_index_1 = outer_index_1 + 2
        inner_index_2 = outer_index_2 + 2
        while inner_index_2 < len(s):
            if s[inner_index_1] == first_pair[0] and s[inner_index_2] == first_pair[1]:
                return True
            else:
                inner_index_1 += 1
                inner_index_2 += 1
        outer_index_1 += 1
        outer_index_2 += 1

def contains_pair_with_letter_between(s):
    s = s.lower()
    current_index = 0
    while current_index < len(s)-2:
        if s[current_index] == s[current_index+2]:
            return True
        current_index += 1

def is_nice(s):
    return contains_nonoverlapping_pairs(s) and contains_pair_with_letter_between(s)

for s in strings:
    if is_nice(s):
        nice_strings.append(s)
    else:
        naughty_strings.append(s)

print(f"There are {len(nice_strings)} nice strings.")