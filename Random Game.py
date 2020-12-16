import random as r

guess = r.randint(0,20)

user = int(input('Enter your guessed number: '))

while True:
    if user != guess :
        if user < guess:
            print("Guess a higher number")
            user = int(input('Enter: '))
            continue
        else:
            print('Guess a lower number')
            user = int(input('Enter: '))
            continue
    else:
        if user == guess:
            print('Congratulations! You guessed a correct number')
            break

import random 

guess = random.randint(0,20)
user = int(input("Enter your Choice: "))
while True:
    if user != guess:
        if user < guess:
            print("Guess Higher!")
            user = int(input("Enter: "))
        else:
            print("Guess Lower!")
            user = int(input("Enter: "))
    else:
        print(f"Congrats! You've guesses the correct number {guess}. ")
        break