#THIS IS A GUESSING GAME

import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0

#     while guess != random_number:
#         guess = int(input(f'Guess a random number between 1 and {x}: '))
#         if guess < random_number:
#             print("Sorry, Guess again, too low")
#         elif guess > random_number:
#             print("Sorry, Guess again, too high")
    
#     print(f'Congratulations. You have guessed the number {random_number} correctly')

#guess(10)


#THE FIRST CODE ALLOWS THE COMPUTER TO SELECT A RANDOM NUMBER BETWEEN 1-10 AND YOU HAVE TO GUESS THE CORRECT NUMBER

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)? ').lower()
        if feedback == 'h':
            high =  guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The AI guessed your number, {guess}, correctly.')



computer_guess(10)




#THE SECOND CODE LETS YOU INPUT A RANDOM NUMMBER BETWEEN 1-10 AND HAVE THE AI GUESS THE NUMBER
