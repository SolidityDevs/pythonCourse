import random
guess = 1
lucky_number = random.randint(1,15)
score = 0
max_guess = 5

while guess < max_guess:
    user_reply = int(input(f"can you guess the lucky number? \nNumbers to guess must be in range 1 - 15\n\n{guess}. What would be the lucky number? "))
    if user_reply >15:
        print('Your answer shouldn\t be greater than 15 ')
    elif user_reply != lucky_number:
        print(f'wrong guess, the lucky number is: {lucky_number} ')
        
        guess += 1
    elif user_reply == lucky_number:
        print(f'Perfect, the lucky number is: {lucky_number} ')
        score += 1
        guess += 1
        
else:
    print(f'Guess game ended\nScored: {score} of {max_guess}\nScore average: {int(score/max_guess * 100)}%')