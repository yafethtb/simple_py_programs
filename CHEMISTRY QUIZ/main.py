from question_base import questions

def quiz():
    ''' Get list of questions and check if the user give the right answer. '''
    # --- Initial variables ---
    point = 0
    total_question = 0
    
    # --- Iterating ---
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

    # --- Show point ---
    print(f"Your point is {point} correct of {total_question} questions.")

    # --- Feedback ---
    if point <= 5:
        print('You might want to learn chemistry again.\n')
    elif point <= 10:
        print("You are on the good track in chemistry.\n")
    elif point <= 15:
        print("Wonderful!\n")
    elif point >= 16:
        print("Superb!\n")

# --- Start here ---
quiz()
