import time

print("Welcome to the timer")

time_limit = int(input("Enter the timer time(in second): "))

for x in range(time_limit, 0, -1):
    seconds = x % 60
    minutes = int(x/60)
    hours = int(x/3600)

    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r")
print("TIMES UP!!")
