from Question import Question
question_prompts = [
    "1) Which of the following is NOT a fully supported Python programming paradigm?\n\
    A: object-oriented | B: structured | C: logic | D: all of the above\n",
    "2) Name the collection of principles that influence the design of Python:\n\
    A: Python Guiding Principles | B: Zen of Python | C: Principles For The Snake | D: The Python's Principles\n",
    "3) Python was first released in:\n\
    A: 1980 | B: 1991 | C: 2000 | D: 2008\n"
]
q = len(question_prompts)
accepted = "ABCDabcd"
questions = [
    Question(question_prompts[0], "c", "C"),
    Question(question_prompts[1], "b", "B"),
    Question(question_prompts[2], "b", "B"),
]
print("This is a multiple choice quiz. Answer correctly to get points.")


def run_test(qstns):
    points = 0
    for question in qstns:
        answer = input(question.prompt)
        if answer not in accepted:
            print("Not an accepted answer!")
        elif answer == question.answer_low or answer == question.answer_up:  # low = lowercase, up = uppercase
            points += 1
            print("Correct!")
        else:
            print("Wrong answer!")
    print(f"Success rate: {round((points/q) * 100, 2)}%")
    print(f"Total points = {points}/{q}")


run_test(questions)
