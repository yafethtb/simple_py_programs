from data_dict import food_list
import random

def game_over(right):
    ''' Game over. Return message how much player guess right. '''
    print(f"Game is over. Your points: {right}.")

score = 0

while True:
    print('-' * 20)
    fact_a, fact_b = random.sample(food_list, k=2) 

    hi_lo = input(
        f"Between {fact_a['Name']} and {fact_b['Name']}\nWhich one have more calories. Type 'a' if {fact_a['Name']} is higher, or 'b' if {fact_b['Name']} is higher:  >  "
    ).lower()

    if (hi_lo == 'a' and fact_a['Calories'] > fact_b['Calories']) or (hi_lo == 'b' and fact_a['Calories'] < fact_b['Calories']):
        print(f"{fact_a['Name']} have {fact_a['Calories']} kcal")
        print(f"{fact_b['Name']} have {fact_b['Calories']} kcal")
        print("You are right.")
        score += 1

        go_on = input("Continue? Press 'y' to continue. Press any other keys to stop. :  > ").lower()
        if go_on == 'y':
            continue
        else:
            game_over(score)
            print('-' * 20)
            break
        
    elif (hi_lo == 'a' and fact_a['Calories'] < fact_b['Calories']) or (hi_lo == 'b' and fact_a['Calories'] > fact_b['Calories']):
        print(f"{fact_a['Name']} have {fact_a['Calories']} kcal.")
        print(f"{fact_b['Name']} have {fact_b['Calories']} kcal.")
        print("You are wrong.")
        game_over(score)
        print('-' * 20)
        break
    else:
        print("Please choose only 'a' or 'b'.")
