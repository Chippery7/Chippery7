import random
num = random.randint(1,101)
while True:
    print('Guess a number 1 through 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('You guessed right')
    elif i > num:
        print('Guess lower')
    elif i < num:
        print('Guess higher')

        
