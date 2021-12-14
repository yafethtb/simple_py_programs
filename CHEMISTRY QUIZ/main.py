from question_base import questions


def quiz():
    ''' Get list of question and check if user answer is correct according to the question shown. '''
    point = 0
    total_question = 0
    for index, question in enumerate(questions, 1):
        print(f"Q{index}: {question['Q']}")
        total_question += 1
        check = input('True or False?  > ').lower()
        print(f"The answer is {question['A']}.\n")
        if check == question['A'].lower():
            print('You are correct\n')
            point += 1
        else:
            print('You are incorrect\n')

    print(f"Your point is {point} correct of {total_question} questions.")

    if point <= 5:
        print('You might want to learn chemistry again.\n')
    elif point <= 10:
        print("You are on the good track in chemistry.\n")
    elif point <= 15:
        print("Wonderful!\n")
    elif point >= 16:
        print("Superb!\n")

quiz()