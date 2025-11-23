print("WELCOME TO THE MALL")
print("PLEASE SELECT FROM THE GIVEN ITEAMS")

iteams = ["APPLES", "GUVA", "SOAP", "OIL", "CONTROLLER", "LAPTOP", "TOOLS", "PENCILS", "PENS"]
prices = [30,60,34,90,23,67,32,84,54]

for i in range(len(iteams)):
    print(f"{i+1}.{iteams[i]} = Rs.{prices[i]}")

cart = []
cart2 = []
select = ''
count = 0
while not select == 'E':
    select = input("SELECT THE ITEAMS TO ADD IN CART (or press E to exit): ")
    if select.isdigit():
        index = int(select)-1
        count += 1
    elif select == 'E':
        break
    else:
        print("Please Enter valid input")
        continue  
    print(f"Okay {iteams[index]} is Added")
    cart.append(iteams[index])
    cart2.append(prices[index])
print(f"You have selected {count} iteams")
for i in range(len(cart)):
    print(f"{i+1}.{cart[i]} = Rs.{cart2[i]}")
total = sum(cart2)
# total = 0
# for i in range (len(cart2)):
#     total = cart2[i]+ total
print("---------------------------------------------------")
print(f"YOUR TOTAL IS RS.{total}")
