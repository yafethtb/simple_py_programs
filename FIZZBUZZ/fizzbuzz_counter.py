print("=" * 8)
print("Let's count how much Fizz, Buzz, and FizzBuzz shown in a certain range of number.\n")

while True:
    # -- input range ---
    number = int(input("Input a range number:  > "))
    if number <= 0:
        print("Please enter a number higher than 0.\n")
        continue
    else:
        print("Thank you.\n")    

    # -- fizz, buzz, fizzbuzz list ---
    fizz_list = [num for num in range(1, number+1) if num % 3 == 0 and num % 15 != 0]
    buzz_list = [num for num in range(1, number+1) if num % 5 == 0 and num % 15 != 0]
    fizzbuzz_list = [num for num in range(1, number+1) if num % 15 == 0]

    # -- number of data of the above lists ---
    fizz = len(fizz_list)
    buzz = len(buzz_list)
    fizzbuzz = len(fizzbuzz_list)

    print (f"In range from 1 to {number}, there are {fizz} times fizz, {buzz} times buzz, and {fizzbuzz} times fizbuzz.")

    # -- show data if user want ---
    show = input("Do you want to see the data? Press 'Y' to  show, or press any other key to not show:  > ").lower()
    if show == 'y':
        print(f"Fizz data: {fizz_list}\nbuzz data: {buzz_list}\nFizzbuzz data: {fizzbuzz_list}.")
        print("=" * 8)
    else:
        print("Okay.")
        print("-" * 8)

    # -- looping the program if user want ---
    loop = input("Do you want to try it again? Press 'Y' to continue, or press any other keys to stop:  > ").lower()
    if loop == 'y':
        print("Let's try it once again.")
        print('-' * 8)
        continue
    else:
        print("Thank you.")
        print("=" * 8)
        break
