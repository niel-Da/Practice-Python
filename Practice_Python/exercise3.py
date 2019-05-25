#Practice Python
#exercise3




# assign the variable 'a' to a list
a = [1,1,2,3,5,8,13,21,34,55,89]


#extra question 1: make a new list with numbers less than 5 in list'a'
#creat an empty list and call it 'b'
b = []
#iterate through 'a' and look for a number less than 5
for lessthanFive in a:
#if this condition of (numbers < 5) is met, then append
#a list of those items in the empty list named 'b' and then print that list
    if lessthanFive < 5:
        b.append(lessthanFive)
        continue
print(b)


#extra question 2: Write it in one line of code
b = [lessthanFive for lessthanFive in a if lessthanFive < 5]
print(b)


#extra question 3: '''Ask the user for a number and return a list that contains
#                     only elements from the original list a that are smaller
#                     than that number given by the user.'''


# request a number from the user
enteredNumber = abs(int(input('Enter a number')))
# 'd' is the max number in list a
#this helps us compare the int user input to int max number in list 
d = max(a, key=int)
#put the outcome of this comparison in an empty list named 'result' 
result = []
for enteredNumber in a: 
#compare enteredNumber to 'd' and then append the outcome to 'result'
    
    if enteredNumber < d+1:
        result.append(enteredNumber)
        print(result)
    
    else:
        print('Your number is higher than the highest number in my list')

