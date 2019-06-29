


# __uthor__ = abrahamd


#Write a program (function!) that takes a list and returns a new list
#that contains all the elements of the first list minus all the
#duplicates.


#define the function 
def list_One():
    #give the function a list
    listOne = [12, 23, 34, 53, 31, 12, 15, 45, 65, 4, 5, 9, 39, 15, 65, 45, 31]
    #create another list from a set of the initial list
    listTwo = list(set(listOne))
    print(listTwo)
    


