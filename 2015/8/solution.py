import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")

#def string_parse(s):
#    l = -2
#    #for i in range(len(s)):
#    i = 0
#    while i < len(s):
#        #print(f"Processing {s[i]}")
#        if s[i] == '\\':
#            #print(f"processing {s[i]}")
#            if s[i+1] == '\\' or s[i+1] == '"':
#                #print(f"processing {s[i+1]}")
#                i += 2
#            elif s[i+1] == 'x':
#                i += 4
#        else:
#            i += 1
#        l += 1
#    return l

def string_encode(s):
    l = 2
    i = 0
    while i < len(s):
        if s[i]== '"' or s[i] == '\\':
            l += 1
        l += 1
        i += 1
    return l

total_code_representation_length = 0
total_string_length = 0
total_encoded_string_length = 0
gift_list = dict()
#for line in lines: 
#    code_representation_length = len(line)
#    string_length = string_parse(s=line)
#    total_code_representation_length += code_representation_length
#    total_string_length += string_length
#    gift_list[line] = []
#    print(f"Processing {line}: code length: {code_representation_length}, string length: {string_length}")
for line in lines: 
    code_representation_length = len(line)
    total_code_representation_length += code_representation_length
    encoded_string_length = string_encode(s=line)
    total_encoded_string_length += encoded_string_length
    
#print(f"Total no of chars in code representations: {total_code_representation_length}")
#print(f"Total no of chars in strings: {total_string_length}")
#print(f"Code repre minus string literals: {total_code_representation_length - total_string_length}.")
print(f"Code repre minus string literals: {total_encoded_string_length - total_code_representation_length}.")