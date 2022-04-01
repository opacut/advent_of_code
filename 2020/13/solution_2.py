import os
import pdb
import signal
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    pdb.set_trace()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

line_to_process= lines[1].split(",")
found = False
min_timestamp = min([int(y) for y in line_to_process if y != 'x'])
max_timestamp = max([int(y) for y in line_to_process if y != 'x'])
#timestamp = int(line_to_process[0])
timestamp = 400110695957620
#timestamp = 0
# already visited:
# 100124231682935
# 100156344449411
# 100156771883443
# 400000000000006
# 400017838075646
# 400072879432640
# 400110695957620
# 200000000000000 is too low
# 500000000000000 gave no hint
# 600000000000000 gave no hint
found_timestamp = None
notit = True
while not found:
    # re-stated, the problem says "timestamp such that timestamp+index is congruent to index modulo initial_list[index]"
    # tmstmp ≡ 0 mod 7
    # tmstmp ≡ 12 mod 13
    # tmstmp ≡ 55 mod 59
    # tmstmp ≡ 25 mod 31
    # tmstmp ≡ 12 mod 19
    # print(f"Investigating timestamp {timestamp}")
    found_list = [False]*(len(line_to_process)-1)
    found_list.insert(0, True)
    for index, number in enumerate(line_to_process):
        if number == 'x':
            found_list[index] = True
            continue
        if (timestamp+index)%int(number)==0:
            found_list[index] = True
    found = all(found_list)
    #pdb.set_trace()
    if found:
        found_timestamp = timestamp
    #pdb.set_trace()
    timestamp += int(line_to_process[0])
    #pdb.set_trace()
    timestamp = int(((int(timestamp/max_timestamp)*max_timestamp)+max_timestamp)/int(line_to_process[0]))*(int(line_to_process[0]))
    #pdb.set_trace()
    #for index, number in enumerate(line_to_process):
    #pdb.set_trace()
    ### #found_list = [int(timestamp%int(number))==(int(number)-index) for index, number in enumerate(line_to_process) if number!='x']
    ### found_list = list()
    ### for index, number in enumerate(line_to_process):
    ###     if number != 'x':
    ###         a = int(timestamp%int(number))
    ###         b = (int(number)-index)%int(number)
    ###         pdb.set_trace()
    ###         c = a == b
    ###         pdb.set_trace()
    ### #pdb.set_trace()
    ### # tmstmp%number=number-index
    ### found = all(found_list)
    ### if found:
    ###     if not notit:
    ###         found_timestamp = timestamp
    ###     notit = False
    ### timestamp += int(line_to_process[0])
    ### timestamp = int(((int(timestamp/max_timestamp)*max_timestamp)+max_timestamp)/int(line_to_process[0]))*(int(line_to_process[0]))


print(f"Found! It's {found_timestamp}")