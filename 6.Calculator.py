print("Welcome to the calcuclator")
x = float(input("Enter first value: "))
y = float(input("Enter the second value: "))
opp = input("Please Enter which operation you want to peform: (+,-,*,/)")

if opp == '+':
    z = x+y
    print(f"Additon is: {z}")
elif opp == '-':
    z = x-y
    print(f"Subtraction is: {z}")
elif opp == '*':
    z = x*y
    print(f"Multiplication is: {z}")
elif opp == '/':
    z = x/y
    print(f"Division is: {z}")
else:
    print("Enter the valid operator")    