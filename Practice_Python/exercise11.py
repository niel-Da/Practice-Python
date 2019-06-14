#get a munber from the user (converted to an integer
#and an absolute number), then put in a variable
#num = abs(int(input('Enter a number')))

#get a range of number starting from 1 up to the
#number entered by user, by incrementing by 1
#lrange = list(range(1,num+1))

#create an empty list
primeList = []
#iterate through range of numbers in lrange
for numPrime in range(2,21):
    naPrime = True
    #condition
    for num in range (2, numPrime):
        if numPrime % num == 0:
            naPrime = False
    if naPrime:
            
        #append output to the empty list divisor
        primeList.append(naPrime)
print (primeList)




# Initialize a list
primes = [] 
for possiblePrime in range(2, 21):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
      
    if isPrime:
        primes.append(possiblePrime)

print (primes)
