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

# Defines functions to add grades to storing system
def take_classwork(assignment_name:str, grade:float):
    classworks[assignment_name] = grade

def take_quiz(assignment_name:str, grade:float):
    quizzes[assignment_name] = grade

def take_test(assignment_name:str, grade:float):
    tests[assignment_name] = grade

take_classwork("homework assignment", 100.0)
take_classwork("hw", 95.0)
take_classwork("homew", 0.0)
print(classworks)
print(list(classworks.values()))

classwork_average = sum(list(classworks.values()))/len(list(classworks.values())) if len(list(classworks.values())) > 0 else 0
quiz_average = sum(list(quizzes.values()))/len(list(quizzes.values())) if len(list(quizzes.values())) > 0 else 0
test_average = sum(list(tests.values()))/len(list(tests.values())) if len(list(tests.values())) > 0 else 0

# if classworks, quizzes, tests are present
if len(classworks) > 0 and len(quizzes) > 0 and len(tests) > 0:
    grade_average = (classwork_average * 0.25) + (quiz_average * 0.35) + (test_average * 0.40)

# if classworks, quizzes are present
elif len(classworks) > 0 and len(quizzes) > 0 and len(tests) == 0:
    grade_average = (classwork_average * 0.58333) + (quiz_average * 0.41666)

# if classworks, tests are present
elif len(classworks) > 0 and len(quizzes) == 0 and len(tests) > 0:
    grade_average = (classwork_average * 0.38333) + (test_average * 0.61666)

# if classworks are present
elif len(classworks) > 0 and len(quizzes) == 0 and len(tests) == 0:
    grade_average = classwork_average

# if quizzes, tests are present
elif len(classworks) == 0 and len(quizzes) > 0 and len(tests) > 0:
    grade_average = (quiz_average * 0.46666) + (test_average * 0.53333)

# if quizzes are present
elif len(classworks) == 0 and len(quizzes) > 0 and len(tests) == 0:
    grade_average = quiz_average

# if tests are present
elif len(classworks) == 0 and len(quizzes) == 0 and len(tests) > 0:
    grade_average = test_average

print(classwork_average)
print(grade_average)