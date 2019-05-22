import time
import datetime


#This program is meant to predict what year a user will be 100 years old using the input provided by user
    
#ask user for their name
name = (input('What is your name:'))

#ask user for their currrent age
currentAge = int(input('what is your age:'))

#number of times user wants message to be reprinted
numberofRepeat = int(input('Number of times you want this repeated:'))

#what is the currect year
currentYear = int(datetime.datetime.now().year)
    
#calculate unknown year by subtracting current age from current year and then add 100 to it
year = (currentYear - currentAge)+100
#set counter to 0 and loop through the number of times the user entered
counter = 1
while counter <= numberofRepeat:
    
#output message to user
    print(name,'You will be 100 years old in year', year,)
    counter += 1
    




