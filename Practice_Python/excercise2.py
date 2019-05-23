#practice python
#excercise2


import time
import os



#define a clear screen function
def clear():
    os.system( 'cls' )

#ask user for a number 
num = int(input('Enter a number:'))

#check for the "even or odd" condition and print message
if num % 2 == 0:
    print(num, '(The number you entered is an even number)')
    if num % 4 == 0:
        print (num, '(...and also a multiple of 4)')
else:
    print(num, '(The number you entered is an odd number)')

#let the program pause for some secs before requesting a set of number
time.sleep(1)
print('.')
time.sleep(2)
print('..')
time.sleep(2)
print('...')
#ask user for a new set of number
num1 = int(input('Enter another number:')) 
check = int(input('...and yet another number:'))
if num1 % check == 0:
    print('You entered',num1,'and',check,'.',
          'Did you know ', check, 'divides into ', num1, 'evenly?')
else:
    time.sleep(1)
    print('I think you just broke my computer.')
    time.sleep(2)
    #clear()
    clear()
