import os
import pdb

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    lines += f.read().split("\n")
    lines.pop()

class Rule:
    def __init__(self, init_string):
        self.name = init_string[0]
        self.rule_string = init_string.split(": ")[1]
        self.possible_interpretations = self.rule_string.split(" | ")
        
    @property
    def is_terminal(self):
        for interpretation in self.possible_interpretations:
            for symbol in interpretation.split(" "):
                if not "\"" in symbol:
                    return False
        return True

rules = list()
words = list()
for line in lines:
    if ":" in line:
        rules.append(Rule(init_string=line))
    elif line == "":
        continue
    else:
        words.append(line)

print(f"Rules: {[f'{rule.name}: {rule.rule_string}' for rule in rules]}")
print(f"Words: {words}")
#pdb.set_trace()
#S = A A C
#B = A C
C = ["ababbbbb", "abababbb", "abaaaaab", "ababbaab", "ababaaab", "abbbbbab", "abbaabab", "abbbbaab", "abbbaaab", "abbabaab", "abbaaaab", "abbabbbb", "abbbbabb", "abbbaabb", "aabababb", "aabaaabb", "aabaabab", "aabaabbb", "aabbaaab", "aabbbbab", "aabbabab", "aabbaabb", "aabbbbbb", "aabbbabb", "aaaaabab", "aaababab", "aaabbaab", "aaabbbab", "aaaaaabb", "aaababbb", "aaabaabb", "baababbb", "bbbaabbb", "bbaaabbb", "bbabbbbb", "bababbbb", "baaabbbb", "bbabbabb", "baabbabb", "baaababb", "bbbababb", "bbaababb", "babaaabb", "baaaaabb", "baabaabb", "bbbbaabb", "bbabaabb", "bbbabbab", "bbbaabab", "bbabbbab", "bbababab", "babaabab", "baaaabab", "baabbbab", "baababab", "babaaaab", "bbaaaaab", "bbbbaaab", "babbaaab", "bbaabaab", "bababaab", "baabbaab", "baaabaab", "baaaabaa", "baabbaaa", "baabaaaa", "baaabaaa", "baaaaaaa", "babbbaaa", "babbaaaa", "babbbbba", "babbbaba", "baabbaba", "baabaaba", "baaabbba", "baaababa", "baaaabba", "baaaaaba", "bbbbabaa", "bbbbbaba", "bbbbbaaa", "bbbababa", "bbbabaaa", "bbbaaaaa", "bbbaabba", "bbbaaaba", "bbabbbba", "bbababba", "bbaabbaa", "bbaaabaa", "bbabaaaa", "bbabbbaa", "bbababaa", "ababbbaa", "abaaabaa", "ababaaaa", "abaaaaaa", "abbbabaa", "abbaaaaa", "abbabbaa", "abbaabaa", "aaababaa", "aaaaaaaa", "aaaabbaa", "aaaabaaa", "aabbbbaa", "aababbaa", "aabaaaaa", "aabbbaaa", "aabbaaaa", "aabbabba", "aaaaabba", "abbbabba", "abbaabba", "abbbbbba", "abbabbba", "aaaabbba", "aabbbbba", "aababbba", "aabbaaba", "aaaababa", "aabbbaba", "aaabbaba", "ababaaba", "abbaaaba", "abaababa", "abbbbaba", "ababbaba"]
A = ["aaabbbba", "aaababba", "aabaabba", "abababba", "ababbbba", "abaaabba", "abaabbba", "abaaaaba", "abbababa", "abbbaaba", "aabababa", "aabaaaba", "aaabaaba", "aaaaaaba", "aaabaaaa", "aaabbaaa", "aababaaa", "ababbaaa", "abaabaaa", "abbabaaa", "abbbaaaa", "abbbbaaa", "aaabbbaa", "aaaaabaa", "aabbabaa", "aabaabaa", "abbbbbaa", "abaabbaa", "abababaa", "baabbbba", "baababba", "babbabba", "babbaaba", "bababbba", "babababa", "babaabba", "babaaaba", "bbabbaba", "bbabaaba", "bbaabbba", "bbaababa", "bbaaabba", "bbaaaaba", "bbbbaaba", "bbbabbba", "bbbbabba", "bbbbbbba", "bababaaa", "babaaaaa", "babbbbaa", "babbabaa", "bababbaa", "babaabaa", "baaabbaa", "baababaa", "baabbbaa", "bbbbaaaa", "bbbaabaa", "bbbbbbaa", "bbbabbaa", "bbabbaaa", "bbaabaaa", "bbaaaaaa", "ababbabb", "ababaabb", "abaabbbb", "abaababb", "abaaabbb", "abaaaabb", "abbababb", "abbaaabb", "abbaabbb", "abbbbbbb", "abbbabbb", "aaabbabb", "aaaababb", "aababbbb", "aabbabbb", "aaaaabbb", "aaabbbbb", "aaaabbbb", "abaabaab", "abbabbab", "abbbabab", "ababbbab", "abababab", "abaabbab", "abaaabab", "aaabaaab", "aaaaaaab", "aaaabbab", "aaaabaab", "aababbab", "aabaaaab", "aabbbaab", "aababaab", "babbaabb", "babbbabb", "babababb", "babbbbbb", "baabbbbb", "baaaabbb", "babbabbb", "babaabbb", "babbbaab", "baabaaab", "baaaaaab", "baaabbab", "bababbab", "babbabab", "babbbbab", "bbaabbab", "bbaaabab", "bbbbbbab", "bbbbabab", "bbabaaab", "bbbaaaab", "bbabbaab", "bbbabaab", "bbbbbaab", "bbbbbabb", "bbbaaabb", "bbaaaabb", "bbaabbbb", "bbababbb", "bbbabbbb", "bbbbabbb", "bbbbbbbb"]

B = list()
for a in A:
    for c in C:
        B.append(a+c)
#print(B)
S = list()
for a in A:
    for b in B:
        S.append(a+b)
#print(S)
correct_words = 0
for word in words:
    if word in S:
        correct_words += 1
print(f"correct words: {correct_words}")