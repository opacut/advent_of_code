import os
import hashlib
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines = f.read().split("\n")[0]

ex1 = 'abcdef'
ex2 = 'pqrstuv'
key1 = '609043'
key2 = '1048970'
result1 = ex1+key1
result2 = ex2+key2

h1 = hashlib.md5(result1.encode()).hexdigest()
h2 = hashlib.md5(result2.encode()).hexdigest()

limit = 10000000
count = 0
while count < limit:
    h = lines+str(count)
    if hashlib.md5(h.encode()).hexdigest()[:6] == '000000':
        print(count)
        break
    count += 1