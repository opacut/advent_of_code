import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = []
with open(os.path.join(__location__, 'input.txt')) as f:
    groups = f.read().split("\n\n")

def process_group_answers_anyone(groups):
    total_questions = 0
    for index, group_string in enumerate(groups):
        members = group_string.split("\n")
        questions = list()
        for member in members:
            for char in member:
                if char not in questions:
                    questions.append(char)
        total_questions += len(questions)
        #print(f"Group number {index+1} contains {len(members)} people; combined, they answered \"yes\" to {len(questions)} questions: {questions}")
    return total_questions

def process_group_answers_everyone(groups):
    total_questions = 0
    for index, group_string in enumerate(groups):
        print(f"\nprocessing group {index}: {group_string}")
        members = group_string.split("\n")
        questions = list()
        initial_questions = list()
        for member in members:
            for char in member:
                if char not in initial_questions:
                    initial_questions.append(char)
        for question in initial_questions:
            for member in members:
                new_add = list()
                if question not in member and question not in questions:
                    break
                if question not in new_add:
                    new_add.append(question)
            questions.append(new_add)
        questions = [item for sublist in questions for item in sublist]
        total_questions += len(questions)
        print(f"In group number {index+1} there are {len(members)} people; \"yes\" to {len(questions)} questions: {questions}")
    return total_questions

print(process_group_answers_everyone(groups=groups))