stop = False

while(not stop):
    play = ('rock','paper','scissor')

    player1 = input('Enter player1\'s name:')
    result1 = input('enter "rock","paper","scissors"')
    print(player1,' You typed '+ result1)
    player2 = input('Enter player2\'s name:')
    result2 = input('enter "rock","paper","scissors"')
    
    print(player2, ' You typed '+ result2)


    if result1 == "rock" and result2 == "scissors":
        print('player1 wins!\n \n')
    elif result1 == "scissors" and result2 == "rock":
        print('player2 wins!\n \n')
    elif result1 == "rock" and result2 == "paper":
        print('player2 wins!\n \n')
    elif result1 == "paper" and result2 == "rock":
        print('player1 wins!\n \n')
    elif result1 == "paper" and result2 == "scissors":
        print('player2 wins!\n \n')
    elif result1 == "scissors" and result2 == "paper":
        print('player1 wins!\n \n')
        
    else:
        print('It\'s a tie!\n \n')

    print('Do you want to play again:')
    answer = input('Enter "yes" or "no" if you want to play again: ')
    if answer == "yes":
        print('Ok! Lets try again')
    else:
        answer == "no"
        stop = True
        print('Thanks for playing')
    


