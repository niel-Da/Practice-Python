stop = False
#begin a while loop
while(not stop):
#play options
    play = ('rock','paper','scissor')
#request user inputs and confirm what user entered
    player1 = input('Enter player1\'s name:')
    result1 = input('enter "rock","paper","scissors"')
    print(player1,' You typed '+ result1)
    player2 = input('Enter player2\'s name:')
    result2 = input('enter "rock","paper","scissors"')
    
    print(player2, ' You typed '+ result2)
#check if the play results from player1 and player2 meet this conditions or else jump to the else statment
    if result1 == result2:
        print('GAME OVER. It\'s a tie!\n \n')
    elif result1 == "rock" and result2 == "scissors":
        print('GAME OVER. player1 wins!\n \n')
    elif result1 == "scissors" and result2 == "rock":
        print('GAME OVER. player2 wins!\n \n')
    elif result1 == "rock" and result2 == "paper":
        print('GAME OVER. player2 wins!\n \n')
    elif result1 == "paper" and result2 == "rock":
        print('GAME OVER. player1 wins!\n \n')
    elif result1 == "paper" and result2 == "scissors":
        print('GAME OVER. player2 wins!\n \n')
    elif result1 == "scissors" and result2 == "paper":
        print('GAME OVER. player1 wins!\n \n')
        
    else:
        print('Something went wrong, please check your spelling and try again. \n \n')
#ask user if they want to play again. if 'yes' restart game. if no end game
    print('Would you like to play again:')
    answer = input('Enter "yes" or "no" if you want to play again: ')
    if answer == "yes":
        print('Ok! Lets try again')
    else:
        answer == "no"
        stop = True
        print('Thanks for playing')
    


