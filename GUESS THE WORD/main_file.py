import random

# --- OPEN WORDS DATABASE ---
with open('words.txt', mode = 'r') as file:
    the_file = file.read()
    wordlist = the_file.splitlines()
    # --- 'words.txt' is a list of words I took from https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/ ---

# --- CHOOSE A WORD TO BE GUESSED ---
chosen_word = random.choice(wordlist)
show = ["__" for i in chosen_word]

# --- OPENING ---
print("Hello, Player One! Wanna play the guessing word?\n")
print("Here are the blank spots. Try to guess what letters to fill the blanks.\n")
print(show)
print("Let's get started!\n")

# --- GAME CONDITIONS ---
end_of_game = False
life_point = 5 

# --- MAIN PROCESS ---
while end_of_game == False:
    # Will always looping if all letter are not guessed.
    print("=" * 8)
    guess = input("Guess a letter: ").lower()
                
    for idx, val in enumerate(chosen_word):
        letter = val
        if guess == letter:
            show[idx] = letter
            win = len([i for i in show if i != "__"])
    
    print(show)

                
    #  --- GAME POINT ---
    if guess in show:
        # Will tell player that they guess it right
        print("\nYou've guess it!")
        print(f"You guess {win} letter(s).\n")
    else:
        # --- Will 'punish' player if they are guessing wrong letter ---
        life_point -= 1
        print(f"\nWrong guess. You have {life_point} more chance.\n")        
        if life_point <= 0:
            print("You lose.\n")
            print(f"The word is {chosen_word.upper()}.\n")
            print("=" * 8)
            break           
    
    # --- checking if no more blank space leeft ---
    if '__' not in show:
        end_of_game = True
        print("You win!")
    else:
        print("Let's continue.")
    
    
        
    
    
    
    


