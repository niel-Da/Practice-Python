#get a munber from the user (converted to an integer
#and an absolute number), then put in a variable
num = abs(int(input('Enter a number')))

#get a range of number starting from 1 up to the
#number entered by user, by incrementing by 1
lrange = list(range(1,num+1))

#create an empty list
divisor = []
#iterate through range of numbers in lrange
for number in lrange:
    #condition
    if num % number == 0:
        #append output to the empty list divisor
        divisor.append(number)
print (divisor)
