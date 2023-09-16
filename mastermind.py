import os
import time
import random

colorList = ["red","green","blue","yellow",
             "brown","orange","magenta","cyan"]

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If computer is running windows use cls
        command = 'cls'
    os.system(command)

def mainMenu():
    print("\n\t\tMastermind Game\n\t1. Play\n\t2. Rules\n\t3. Exit")
    while True:
        try:
            menuInput = int(input("\tMenu: "))
            if menuInput == 1:
                print("\n\tWelcome to the game!")
                randomize()
            elif menuInput == 2:
                rules()
            elif menuInput == 3:
                print("You exited the game!")
                os.system("pause")
                exit()
            else:
                print("Try again.\n")
                continue
            break
        except ValueError:
            print("Try again.\n")
            continue

def rules():
    print("\n\t\tWelcome to Mastermind Game!")
    print("\t- In the game of Mastermind, the player's objective is to")
    print("\t  guess a secret combination of four colors\n\t  chosen from a set of eight available colors:")
    print("\n\t\t[Red]    [Green]   [Blue]     [Yellow]")
    print("\t\t[Brown]  [Orange]  [Magenta]  [Cyan]\n")
    print("\t- After each guess, feedback is provided in the form of\n\t  white and black pegs.") 
    print("\t- A white peg signifies a correct color\n\t  in the guessed combination but in the wrong position,")
    print("\t  while a black peg indicates both the correct color\n\t  and the correct position.")
    print("\t- The player continues making guesses, using the feedback")
    print("\t  to deduce the secret combination within 10 number of attempts.")
    print("\t- The goal is to solve the puzzle and reveal the hidden code.")
    time.sleep(3)
    mainMenu()

def randomize():
    global ans0,ans1,ans2,ans3
    ans0 = random.choice(colorList)
    ans1 = random.choice(colorList)
    ans2 = random.choice(colorList)
    ans3 = random.choice(colorList)
    play()

def play():
    global attempt
    attempt = 0

    with open("answer.txt","w") as output:
        output.write("["+ans0+"] "+"["+ans1+"] "+
                    "["+ans2+"] "+"["+ans3+"] ")


    while attempt <= 9:
        print("\n\n\t---------------------------------------")
        print("\n\tAttempt: "+str(attempt+1))
        print("\n\tYour Guess:-")
        time.sleep(1)
        playerGuess = [input("\t1st Box: "), input("\t2nd Box: "), 
                    input("\t3rd Box: "), input("\t4th Box: ")]

        playerAns0 = playerGuess[0].casefold()
        playerAns1 = playerGuess[1].casefold()
        playerAns2 = playerGuess[2].casefold()
        playerAns3 = playerGuess[3].casefold()

        print("\n\t"+
            "["+playerAns0+"] "+"["+playerAns1+"] "+
            "["+playerAns2+"] "+"["+playerAns3+"] ")
        
        # Hint conditions
        if (playerAns0 in [ans1,ans2,ans3]) and (playerAns0 != ans0):
            print("\tWhite",end="")
        elif (playerAns0 not in [ans1,ans2,ans3]) and (playerAns0 == ans0):
            print("\tBlack",end="")

        if (playerAns1 in [ans0,ans2,ans3]) and (playerAns1 != ans1):
            print("\tWhite",end="")
        elif (playerAns1 not in [ans0,ans2,ans3]) and (playerAns1 == ans1):
            print("\tBlack",end="")

        if (playerAns2 in [ans0,ans1,ans3]) and (playerAns2 != ans2):
            print("\tWhite",end="")
        elif (playerAns2 not in [ans0,ans1,ans3]) and (playerAns2 == ans2):
            print("\tBlack",end="")

        if (playerAns3 in [ans0,ans2,ans1]) and (playerAns3 != ans3):
            print("\tWhite",end="")
        elif (playerAns3 not in [ans0,ans2,ans1]) and (playerAns3 == ans3):
            print("\tBlack",end="")

        if (playerAns0 != ans0) or (playerAns1 != ans1) or (
            playerAns2 != ans2) or (playerAns3 != ans3):
            attempt += 1
        # Winning condition
        elif (playerAns0 == ans0) and (playerAns1 == ans1) and (
            playerAns2 == ans2) and (playerAns3 == ans3):
            win()
            break

    lose()

def win():
    print("\n\tYou Win!")
    time.sleep(5)
    clearConsole()
    mainMenu()

def lose():
    print("\n\tYou Lose!")
    print("\tThe answer is"+" ["+ans0+"] "+"["+ans1+"] "+"["+ans2+"] "+"["+ans3+"] ")
    time.sleep(5)
    clearConsole()
    mainMenu()

mainMenu()