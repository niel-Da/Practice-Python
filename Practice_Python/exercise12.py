#exercise12
#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#and makes a new list of only the first and last elements of the given list. For practice,
#write this code inside a function.

#define your function 
def firstAndLast():
    #declare your list
    justList = [28, 2, 11, 39, 5, 10, 15, 20, 25, 44, 102]
    #declare first elemet of list
    justLista = justList[0]
    #declare second element of list
    justListb = justList[10]
    #delare new list with first and second element of list
    newList = [justLista,justListb]
    #print new list
    print(newList)
#call the function
firstAndLast()
