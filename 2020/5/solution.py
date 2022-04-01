import os
import pdb
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")

N_ROWS=list(range(0,128))
N_COLUMNS=list(range(0,8))


def decode_row(row):
    interval = N_ROWS
    for code in row:
        if code == 'F':
            interval = list(range(interval[0],interval[int(len(interval)/2)]))
        else:
            interval = list(range(interval[int(len(interval)/2)], interval[-1]+1))
    return interval[0]

def decode_column(column):
    interval = N_COLUMNS
    for code in column:
        if code == 'L':
            interval = list(range(interval[0],interval[int(len(interval)/2)]))
        else:
            interval = list(range(interval[int(len(interval)/2)], interval[-1]+1))
    return interval[0]

def construct_plan():
    plan = []
    for _ in N_ROWS:
        row = [' ']*8
        #pdb.set_trace()
        plan.append(row)
    #pdb.set_trace()
    return plan

def get_seat_info(lines):
    seat_ids = []
    plan = construct_plan()
    for line in lines:
        #BBFFBBFRLL
        row=decode_row(line[:7])
        column=decode_column(line[7:])
        seat_id = int(row)*8+int(column)
        seat_ids.append(seat_id)
        plan[row][column] = 'X'
        #print(f"{line}: row {row}, column {column}, seat ID {seat_id}")
    print(plan)
    print("Free seats:")
    for row_index, row in enumerate(plan):
        if 'X' not in row:
            continue
        for seat_index, seat in enumerate(row):
            if seat != "X":
                print(f"row {row_index}, column {seat_index}, ID {int(row_index*8+seat_index)}")
    print(f"Max seat_id is {max(seat_ids)}")

get_seat_info(lines=lines)