# 1.Show balance 
# 2. Deposite
# 3. Withdraw

bal = 20000
def balance():
    global bal
    print(f"Your balance is {bal}")

def Withdraw():
    global bal
    amu = int(input("Enter amount to Withdraw: "))
    if(amu > bal):
        print("INSUFFICIENT BALANCE!!!!")
    elif(amu <= bal):
        print(f"You have Withdrawn :{amu} Sucessfully!!! ")
        bal = bal - amu
        print(f"YOUR CURRENT BALANCE IS : {bal}")

def Deposite():
    global bal
    add = int(input("Enter amount to Deposite: "))
    bal = bal + add
    print(f"YOUR CURRENT BALANCE IS : {bal}")

print("WELCOME TO THE ANDHA BANK")

f=0
while(f!=1):
    print("1.Show balance\n2.Withdraw\n3.Deposite")
    opt = int(input("Please select from the given option: "))
    match opt:
        case 1:
            balance()
            print("---------------------------------------------------------------------")
            print("Do you want to Continue press 'Y'\nDo you want to Exit press 'E'")
            got = input("ENTER: ")
            print("---------------------------------------------------------------------")
            if(got == 'Y'):
                continue
            elif(got == 'E'):
                f=1
        case 2:
            Withdraw()
            print("---------------------------------------------------------------------")
            print("Do you want to Continue press 'Y'\n Do you want to Exit press 'E'")
            got = input("ENTER: ")
            print("---------------------------------------------------------------------")
            if(got == 'Y'):
                continue
            elif(got == 'E'):
                f=1
        case 3:
            Deposite()
            print("---------------------------------------------------------------------")
            print("Do you want to Continue press 'Y'\n Do you want to Exit press 'E'")
            got = input("ENTER: ")
            print("---------------------------------------------------------------------")
            if(got == 'Y'):
                continue
            elif(got == 'E'):
                f=1
        case _:
            print("Please Enter the valid option!")
print("Thank you for choosing our BANK!!")