#number_to_code = {
#    0: ['a','b','c','e','f','g'],
#    1: ['c','f'],
#    2: ['a','c','d','e','g'],
#    3: ['a','c','d','f','g'],
#    4: ['b','c','d','f'],
#    5: ['a','b','d','f','g'],
#    6: ['a','b','d','e','f','g'],
#    7: ['a','c','f'],
#    8: ['a','b','c','d','e','f','g'],
#    9: ['a','b','c','d','f','g']
#}
number_to_code = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}
code_to_number = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

class Display:
    def encode(self, number):
        return number_to_code[number]

    def decode(self, code):
        return code_to_number[code]