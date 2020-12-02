import random

import sys

answer = int(random.randint(1, 25))
guess_attempt = 1
tries = []


def welcome():
    welcome = input("Hi! Would you like to play >>>THE SEARCH FOR THE HOLY NUMBER<<<?(Y/N)   ")
    while welcome.lower() != 'y':
        if welcome.lower() == 'n':
            sys.exit("Aww that is too bad! It would have been fun! Maybe next time!")   
        print("I'm sorry, that is not a valid character, please try either Y or N")
        welcome = input("Hi! Would you like to play >>>THE GUESSING GAME<<<?(Y/N)   ")             
    else:
        print("Great! In order to win you will have to guess the correct random number between 1 - 25.")
                
        
def start_the_game(): 
    answer = int(random.randint(1, 25))
    guess_attempt = 1 
    start_game = 0
    while start_game != answer:
        try:
            start_game = int(input("Guess away!   ".format(answer)))
        except ValueError or TypeError:
            guess_attempt += 1
            print("That is right out! Make sure to choose a number between 1 - 25.")
            
        else:
            if start_game < 1 or start_game > 25:
                guess_attempt += 1
                print("That is right out! Make sure to choose a number between 1 - 25.") 
            elif start_game > answer:
                guess_attempt += 1
                print("Hint: It is lower than that!")
            elif start_game < answer:
                guess_attempt += 1
                print("Hint: It is higher than that!")
                      
    if start_game == answer: 
        print("Well guessed! And it only took you {} attempts!".format(guess_attempt))
        tries.append(guess_attempt)
        play_again = input("Would you like to play again?(Y/N)  ")
        while play_again.lower() == 'y':
            print("Good! Or I would have turned you into a newt!(You'd get better)")
            print(min(tries),"is the current high score. Can you beat it?")
            start_the_game()
        else:    
            print("Aww that is too bad! Thanks for playing!")
            sys.exit("Remember: Always look on the bright side of life!")    
                       

welcome()

start_the_game()



    


    





