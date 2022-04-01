import collections
from classes import Board

f = open("4/input.txt", "r")
lines = [l for l in f.read().split("\n\n")]
for line in lines:
    print(line)
print(lines)
drawn_numbers = lines[0].split(",")
print(f"Drawn numbers: {drawn_numbers}")
boards = [Board(data=board.split("\n")) for board in lines[1:]]
for board in boards:
    print(f"Board: {board}")

found = False
for n in drawn_numbers:
    if found:
        break
    #print(f"Drawing number...{n}!")
    for board in boards:
        #if board.process_number(int(n)):
        #    found = True
        #    break
        if not board.closed:
            board.process_number(int(n))
        