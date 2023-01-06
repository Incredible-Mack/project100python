import random

print("Guessing Game")
print("""Rules: Try to predict the number I will choose between 1 - 10""")

def continuegame():
    if Wrong == True: 
        choice =  input("""Do You wish to try again Y/N
        Y to continue and N to Quit: """)
        # choice = str(choice)
        if choice.lower() == "y" :
            guess = input("Maka a Guess: ")
            guessing(guess)
        elif choice.lower() == 'n' :
            print("The End")
            exit()
        else:
            print("Wrong Choice... The end")
            exit()


guess = input("Maka a Guess: ")
guess = int(guess)
def guessing(guess):
    comGuess = random.randint(0, 9) + 1
    if comGuess == guess:
        print("You Win, Congratulation")
        continuegame()
    else:
        global Wrong;  Wrong = True
        print("Wrong!!!.....My Guess is ", comGuess)
        continuegame()
guessing(guess)







