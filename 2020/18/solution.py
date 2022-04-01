import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'proof.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

def evaluate(expression, val=0):
    expression = expression.split(" ")
    result = int(expression[0])
    while len(expression)>=3:
        left = expression.pop(0)
        operator = expression.pop(0)
        right = expression.pop(0)
        if operator == "+":
            result += int(right)
        if operator == "*":
            result = result*int(right)
        expression.insert(0,result)
    return result



for ex in lines:
    print(evaluate(expression=ex))