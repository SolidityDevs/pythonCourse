import random
random_num = random.randint(1, 15)  # generating random number between 1 and 15
tries = 5   # number of times the user will have to make the guess
for num_tries in range(5):
    try:
        guess_num = int(input("Can you guess the number between 1 - 15: "))     # user to guess number
        while guess_num in range(1, 15):
            if guess_num == random_num:
                print(guess_num, "!!", "Your guess is right.")  # output when user guesses right
                exit()
            else:
                print("Oops!, your guess was wrong")
                tries -= 1      # number of tries left for the user
                print("You have", tries, "more tries remaining.")
                if tries == 0:
                    print("You have exhausted your tries.")
                    exit()
                break
        else:
            print(guess_num, "is out of range")     # output when the user types in a number out of the given range
    except ValueError:
        print("This is not valid, you need to input a number")      # output when the user gives a non number input
