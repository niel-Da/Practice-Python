#__author__ = dabraham

#Exercise7
#Let’s say I give you a list saved in a variable:
#   a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#   Write one line of Python that takes this list
#   a and makes a new list that has only the even
#   elements of this list in it.

#create a list with the variable 'a'
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#iterate through each element of a and print if 2 modulo is equal to 0 
b = [element for element in a if element % 2 == 0]
print(b,'\n','\n')








#Bonus for my reference
a = [2,5,76,5,9,34,2,68,45]

print ([element for element in a if (element > 2) % 2 == 0])
print([element for element in a if (element > 2) % 2 != 0],'\n','\n')



import random

numlist = []
list_length = random.randint(5,15)


while len(numlist) < list_length:
    numlist.append(random.randint(1,75))
    

evenlist = [number for number in numlist if number % 2 == 0] 

print(numlist)
print(evenlist)

#read-up more on list comprehension


