# Write a function that asks the user for a string containing multiple words. Print
## back to the user the same string, except with the words in backwards order.


#ask user for long string
a = input('Enter a long string or sentence: ')

#define your function
def reverse_String(a):
        #split long sting by whitespace delimiter and assign it to b
	b = a.split()
	#create an empty list
	d = []
	#iterate through b an then insert each word at the begining of d at index 0
	for word in b:
	    d.insert(0,word)
	    #assemble delimited string and print
	print( ' '.join(d))
            
    

reverse_String(a)

