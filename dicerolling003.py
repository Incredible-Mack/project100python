''''Dice Rolling'''
import random
import os

def selectDice():
    numDice = input("Enter the number of dice: ")
    try:
        dice = ['1','2','two','one']
        if numDice not in dice:
            raise ValueError("Only 1 or 2 dices allowed")
        else: 
            return numDice
    except ValueError as err:
         print(err)
         exit()

def rolldice():
   
    minNum = 1; maxNum = 6
    rollagain = 'y'

    while rollagain.lower() == 'y' or rollagain.lower() == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        diceselecte = selectDice()

        if diceselecte == '1' or diceselecte == 'one':
            diceone = random.randint(minNum,maxNum)
            print("Rolling Dice...")
            print("You rolled : ", diceone)
            rollagain = input("Roll Again: ")
        else:
            diceone = random.randint(minNum,maxNum)
            dicetwo = random.randint(minNum,maxNum)
            print("Rolling Dice...")
            print("You rolled : ", diceone)
            print("You rolled : ", dicetwo)

            print("Total:", int(diceone) + int(dicetwo))
            rollagain = input("Roll Again: ")
       

rolldice()
