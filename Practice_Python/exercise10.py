import random


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

inBoth = set(i for i in a if i in b)

print(inBoth)








#print(random.sample(range(1,100),9))
#print(random.sample(range(1,100),13))

#a=random.sample(range(1,100),19)
#b=random.sample(range(1,100),31)

#print(set(x for x in a if x in b))
