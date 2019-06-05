import random





a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 35]



#turn the list into a set in order to compare the elements of both sets
ac = set(a)
bc = set(b)
#put the common number in a variable
commonNumbers = ac.intersection(bc)
#create a list of the commonNumbers
c = list(commonNumbers)
#print Common numbers as a set and as a list
print(c,'are list of numbers common in list a and b \n')

#Bonus Points
#generate two random lists
d = random.sample(range(25, 35), 10)
e = random.sample(range(2,45),15)

#convert list to a set
dList = set(d)
eList = set(e)
#get the insection of the set
cn = dList.intersection(eList)
#convert set back to list
fList = list(cn)
#print list
print(fList,'are list of numbers common in the two random lists ' )






 
