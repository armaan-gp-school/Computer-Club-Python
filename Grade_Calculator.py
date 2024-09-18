# ----- Grade Calculator -----

invalid_input = "That was not a valid input."

def take_input(question:str, is_int=False, options=()):
    while True:
        if is_int is False:
            inp = input(question)
        else:
            while True:
                try:
                    inp = int(input(question))
                except ValueError:
                    print(invalid_input)
                else:
                    break
        if len(options) != 0:
            if inp not in options:
                print(invalid_input)
                continue
        return inp
            

# Sets up the storing of assignment grades
classworks = {}
quizzes = {}
tests = {}

classwork_percent = 25
quiz_percent = 35
test_percent = 40

# Defines functions to add grades to storing system
def take_classwork(assignment_name:str, grade:float):
    classworks[assignment_name] = grade

def take_quiz(assignment_name:str, grade:float):
    quizzes[assignment_name] = grade

def take_test(assignment_name:str, grade:float):
    tests[assignment_name] = grade

take_classwork("homework assignment", 100.0)
print(classworks)
print(list(classworks.values()))

classwork_average = sum(list(classworks.values()))/len(list(classworks.values()))
quiz_average = sum(list(quizzes.values()))/len(list(quizzes.values()))
test_average = sum(list(tests.values()))/len(list(tests.values()))

if len(classworks) > 0 and len(quizzes) > 0 and len(tests) > 0:
    grade_average = (classwork_average * 0.25) + (quiz_average * 0.35) + (test_average * 0.40)
elif len(classworks) > 0 and len(quizzes) > 0 and len(tests) == 0:
    grade_average = (classwork_average * 0.)