#exercise6
#Ask the user for a string and print out
#whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)


#ask user for a word
wordEntered = input('Enter a word:')

#loop through entered word to see if it meets condition
for word in wordEntered:
    #condition
    if word[0:] == wordEntered[-1:]:
        print('We have a Palindrome in the word - ',wordEntered)
        
        break
    else:
        print('Sorry. we don\'t have a palindrome in the word - ', wordEntered)
        break

