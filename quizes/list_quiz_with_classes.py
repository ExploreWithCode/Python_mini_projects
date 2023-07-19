from Question import QuestionL
question_prompts = [
    "1) Scandinavian countries: \n",
    "2) European microstates: \n"
]
q = len(question_prompts)
scand_cntrs = ["Norway", "Finland", "Sweden"]
eur_micros = ["Vatican City", "Monaco", "San Marino", "Liechtenstein", "Malta", "Andorra"]
questions = [
    QuestionL(question_prompts[0], scand_cntrs),
    QuestionL(question_prompts[1], eur_micros),
]
print("Find an item in a given list. Use uppercase and lowercase appropriately.")


def que(qstns):
    points = 0
    for question in qstns:
        answer = input(question.prompt)
        if answer.isnumeric():
            print("Not an accepted answer!")
        elif answer in question.lis:
            points += 1
            print("Correct!")
        else:
            print("Wrong answer!")
    print(f"Success rate: {round((points/q) * 100, 2)}%")
    print(f"Total points = {points}/{q}")


que(questions)
