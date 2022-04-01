import collections

f = open("3/input.txt", "r")
lines = [l for l in f.read().split("\n")]
#for line in lines:
#    print(line)
#print(lines)

gamma_rate = ""
epsilon_rate = ""
oxygen_generator_rating = ""
co2_scrubber_rating = ""

def most_frequent(l):
    counter = 0
    num = 1
    #count_ones = l.count("1")
    #count_zeros = l.count("0")
    for i in l:
        curr_frequency = l.count(i)
        if curr_frequency >= counter:
            counter = curr_frequency
            num = i
    #if count_ones >= count_zeros:
    #    return "1"
    #elif count_ones > count_zeros:
    #    return "0"
    return num

def least_frequent(l):
    counter = 0
    num = l[0]
    for i in l:
        curr_frequency = l.count(i)
        if curr_frequency < counter:
            counter = curr_frequency
            num = i
    return num

def binary_to_decimal(b):
    byte_array = bytearray(b, "utf8")
    byte_list = []
    for byte in byte_array:
        binary_representation = bin(byte)
        byte_list.append(binary_representation)
    return str(byte_list)

lines_T = list(map(list, zip(*lines)))
for line in lines_T:
    gamma_rate += most_frequent(line)
    epsilon_rate += collections.Counter(line).most_common()[-1][0]
decimal_gamma_rate = int(gamma_rate, 2)
decimal_epsilon_rate = int(epsilon_rate, 2)
#print("The gamma rate is "+str(gamma_rate)+", which is "+str(decimal_gamma_rate)+", and the epsilon rate is "+str(epsilon_rate)+", which is "+str(decimal_epsilon_rate)+".")
#print("The power consumption is "+str(decimal_gamma_rate*decimal_epsilon_rate)+".")

found = False
destructive_lines = lines.copy()
current_index = 0
final_number = ""
while len(destructive_lines) > 1: 
    #print("Destructive lines: "+str(destructive_lines)+". Current index is "+str(current_index))
    dest_lines_T = list(map(list, zip(*destructive_lines)))
    most = most_frequent(dest_lines_T[current_index])
    #print("Most frequent is "+str(most)+".")
    tmp_lines = destructive_lines.copy()
    for i in reversed(range(len(tmp_lines))):
        #print("i: "+str(i))
        if tmp_lines[i][current_index] != most:
            #print("Deleting index "+str(i)+": "+str(tmp_lines[i]))
            #del destructive_lines[current_index]
            destructive_lines.pop(i)

    current_index += 1
oxygen_generator_rating = int(destructive_lines[0], 2)
#print("FINAL Destructive lines: "+str(destructive_lines)+".")
print("Oxygen generator rating: "+str(oxygen_generator_rating)+".")

found = False
destructive_lines = lines.copy()
current_index = 0
final_number = ""
while len(destructive_lines) > 1: 
    #print("Destructive lines: "+str(destructive_lines)+". Current index is "+str(current_index))
    dest_lines_T = list(map(list, zip(*destructive_lines)))
    most = collections.Counter(dest_lines_T[current_index]).most_common()[-1][0]
    #print("Least frequent is "+str(most)+".")
    tmp_lines = destructive_lines.copy()
    for i in reversed(range(len(tmp_lines))):
        #print("i: "+str(i))
        if tmp_lines[i][current_index] != most:
            #print("Deleting index "+str(i)+": "+str(tmp_lines[i]))
            destructive_lines.pop(i)
    current_index += 1
co2_scrubber_rating = int(destructive_lines[0], 2)
#print("FINAL Destructive lines: "+str(destructive_lines)+".")
print("Oxygen generator rating: "+str(co2_scrubber_rating)+".")
print("Life support rating is "+str(oxygen_generator_rating*co2_scrubber_rating)+".")