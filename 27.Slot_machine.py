import random

option = ('🙈','🙉','🙊')

f=0
x=0
print("WELCOME TO THE WHEEL OF DREAM!!")
print("Rules:")
print("1.Available balance = 50 credits\n2.Each spin costs 5 credit\n3.If you ran out of credit then game is OVER!!\n4.If you win the JACKPOT your credits are doubled")
bal = 50
use = 0
while(f!=1):
    x_1 = random.choice(option)
    x_2 = random.choice(option)
    x_3 = random.choice(option)
    l = input("Press Enter to start spinning And 'E' to Exit:")
    if(l == ''):
        if(bal != 0):
            print(x_1,x_2,x_3)

            if(x_1==x_2==x_3):
                print("HURRAY YOU WIN THE JACKPOT!!🥳")
                bal = bal*2
                f=1
            use = use + 5
            bal = bal - 5
        elif(bal == 0):
            print("Out of credit😟\nGAME OVER!!💀")
            f=1
    elif(l == 'E'):
        f=1
    else:
        print("Enter valid keyword!")

print("---------------------------------------")
print(f"Credits used : {use}")
print(f"Credits left : {bal}")
print("Thanks for coming!!")
