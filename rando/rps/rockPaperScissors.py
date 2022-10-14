import math
import random
import os

userScore = 0
comScore = 0
#dictionary to translate letters to words
choices = {'r':'rock', 'p':'paper', 's':'scissors'}

#list initialization
choiceList = ['r','p','s', 'q']
binList = ['y', 'n']

def rekt():
    print("  rekt lol")
    global comScore
    comScore+=1

def gg():
    print("  gg")
    global userScore
    userScore+=1

#reading function
with open("./rando/rps/rpsData.txt", 'r') as f:
    userScore=int(f.readline())
    comScore=int(f.readline())
    f.close()

#opening for writing
f = open("./rando/rps/rpsData.txt", "w")



os.system('cls' if os.name == 'nt' else 'clear')
print("\nWelcome to the game of all games!!\nType 'q' if you get bored.\n")

userChoice = 'r'

#while the user doesn't press 'quit'
#aka game loop
while userChoice != "q":
    
    userChoice=input("Type your choice ( r / p / s ):\n").lower()
    while userChoice not in choiceList:
        userChoice = input("\nLet's try that again with one of the actual choices ( r / p / s // q quit )\n\n")

    comChoice = choiceList[random.randint(0,2)]
    if(userChoice == "q"): 
        print("\n\nFinal score:\nYou: "+str(userScore)+"\nCOM: "+str(comScore)+"\n") 
        os.system('cls' if os.name == 'nt' else 'clear')
        save = input("SAVE GAME?\nY / N\n\n").lower()
        while save not in binList:
            save = input("\nWe're really doing this right now? At the end of the game?\n\n").lower()
        if(save == 'y'):
            f.write(str(userScore)+'\n'+str(comScore))
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nSaved\n")
            print("\n\nFinal score:\nYou: "+str(userScore)+"\nCOM: "+str(comScore)+"\n") 
        else:  
            f.write("0\n0") 
            print("\nErased\n")
        break
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n+=======================================+\n  You threw "+choices[userChoice]+" and COM threw "+choices[comChoice]+"  ")
    
    match userChoice:
        case "r":
            if comChoice == "p":
                rekt()
            elif comChoice == "s":
                gg()

        case "p":
            if comChoice == "s":
                rekt()
            elif comChoice == "r":
                gg()

        case "s":
            if comChoice == "r":
                rekt()
            elif comChoice == "p":
                gg()
    print("+=======================================+\nCurrent score:\nYou: "+str(userScore)+"\nCOM: "+str(comScore)+"\n\n") 

f.close()