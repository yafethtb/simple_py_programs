from data_dict import food_list
import random

def game_over(right):
    ''' Game over. Return message how much player guess right. '''
    print(f"Game is over. Your points: {right}.")

def result(name_a, name_b, cal_a, cal_b, guess):
    ''' Checking user guess. Return only True or False '''
    print('-' * 20)
    print(f"{name_a} have {cal_a} Kcal.")
    print(f"{name_b} have {cal_b} Kcal.")
    if (guess == 'a' and cal_a > cal_b) or (guess == 'b' and cal_a < cal_b):
        return True
    else:
        return False

score = 0

# Game part
while True:
    print('=' * 20)
    fact_a, fact_b = random.sample(food_list, k=2)
    fact_a_name, fact_b_name, fact_a_cal, fact_b_cal =  fact_a['Name'], fact_b['Name'], fact_a['Calories'], fact_b['Calories']
    
    # Guessing part
    while True:
        hi_lo = input(
            f"Between {fact_a_name} and {fact_b_name}\nWhich one have more calories? Type 'a' if {fact_a_name} is higher, or 'b' if {fact_b_name} is higher:  >  "
        ).lower()
        if hi_lo == 'a' or hi_lo == 'b':
            break
        else:
            print("Please choose only 'a' or 'b'.\n")
            continue
    
    answer = result(fact_a_name, fact_b_name, fact_a_cal, fact_b_cal, hi_lo)

    # Decision part
    if answer is True:
        print("You are right.")
        print('-' * 20)
        score += 1

        go_on = input("Continue? Press 'y' to continue. Press any other keys to stop. :  > ").lower()
        if go_on == 'y':
            continue
        else:
            game_over(score)
            print('=' * 20)
            break
            
    else:
        print("\nYou are wrong.\n")
        game_over(score)
        print('=' * 20)
        break          
        
