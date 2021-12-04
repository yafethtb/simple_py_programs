import random

def guess_choice(random_guess, chance):
    ''' Compare guesses with randomized number created by the program .'''
    while chance > 0:
        print("-" * 8)
        your_guess = int(input("Enter your guess:  > "))         
        if your_guess == random_guess:
            print("You guess it right!")
            print("-" * 8)
            break
        elif your_guess < random_guess:
            print("Your guess is too low.")            
            chance -= 1
            print(f"You have {chance} life point(s) left.")
            print("-" * 8)
        elif your_guess > random_guess:
            print("Your guess is too high!")            
            chance -= 1
            print(f"You have {chance} life point(s) left.")
            print("-" * 8)
    return chance

while True:
    game_on = True
    guess = random.randint(0, 100)
    print("=" * 8)
    print("Let's guess a number between 0 to 100.")

    while game_on:
        difficulty = input("Choose your difficulty level. Press '1' to choose EASY LEVEL, or press '2' to choose HARD LEVEL:  > ")
        if difficulty == '1':
            print("=" * 8)
            print("You have 10 life points. Each wrong guess, you'll lose one life. ")
            life = guess_choice(guess, 10)
            game_on = False
        elif difficulty == '2':
            print("=" * 8)
            print("You have 6 life points. Each wrong guess, you'll lose one life. ")
            life = guess_choice(guess, 6)
            game_on = False
        else:
            print("Please only choose '1' or '2'.")
        
    if life > 0:
        print("=" * 8)
        go_again = input("Would you continue playing? Press 'y' to continue, or press any other keys to stop:  > ").lower()
        if go_again == 'y':
            continue
        else:
            print("Thank you for playing.")
            break
    else:
        print("-" * 8)
        print(f"The right number is {guess}.")
        print("Your life point is 0. You can't continue.")
        print("Thank you for playing.")
        print("=" * 8)
        break