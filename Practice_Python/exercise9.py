#Exercise9


#import the randint submodule from random
from random import randint

#assign random number to a variable called number
number = randint(1,9)

#initialze the variable guess and count to 0
guess = 0
count = 0

#check for while loop condition
while guess != number and guess != "exit":
    #assign user input to the variable guess
    guess = input('Guess a number or type "exit" to exit: ')
    #check if statement condition
    if guess == "exit":
        break
    #convert guess to an integer and assign it to guess
    guess = int(guess)
    #increment count by 1
    count += 1
    #check for another if statement condition and print message
    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high!')
    else:
        print('You got it!')
        print('And it only took you', count, 'tries!')
    



