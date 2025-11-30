import random

colors = ['R','G','B','Y','W','O']
code1 = random.choice(colors)
code2 = random.choice(colors)
code3 = random.choice(colors)
code4 = random.choice(colors)

Ans = [code1 ,code2,code3,code4]
Correct = 0
Incorrect = 0
def game():
    global Correct
    global Incorrect
    for j in range(10):
        Guess = input("Guess: ").upper().split(" ")
        if any(g not in colors for g in Guess):
            print("Invalid colors in guess. Please use only the following colors: ['R','G','B','Y','W','O']")
            continue
        if len(Guess) != 4:
            print("Please enter exactly 4 colors separated by spaces.")
            continue
        for i in range(4):
            if(Ans[i]==Guess[i]):
                Correct += 1
            else:
                Incorrect += 1
        print(f"Correct Position: {Correct} | Incorrect Position: {Incorrect}")
        if (Correct == 4):
            break
        else:
            Correct = 0
            Incorrect = 0
    
    if(Correct == 4):
        for k in range(5):
            print("CONGRATULATIONS!! 🎊🎊")
        print("YOU WON THE GAME!🥳")
        print(F"YOU GUESSED IN {j+1} TRIES")
        print("NOW GET YOUR FAT ASS OUT FROM HERE YOU DICK 🫵😒 ")
    else:
        print("YOU LOSE !! PLEASE TRY AGAIN ☹️")
        print("SUCH A LOSER LOL HAHAHAH 😂🫵")
        print("Go GET BACK TO YOUR MOM YOU POOR 😏 ")

if __name__ == "__main__":    
    print("WELCOME TO THE MASTERMIND GAME YOU HAVE (10) TRIES TO GUESS THE COLOR!\nTHE COLORS YPU CAN USE ARE ['R','G','B','Y','W','O']")
    game()
    print(f"ANSWER WAS: {Ans}")
