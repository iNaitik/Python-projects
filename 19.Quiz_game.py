questions = (("Who was the first President of India?"),
            ("Which planet is known as the 'Red Planet'?"),
            ("Who wrote the national anthem of India?"),
            ("What is the largest ocean in the world?"),
            ("In which year did India gain independence?"))

options_1 = (("a) Dr. B.R. Ambedkar","b) Dr. Rajendra Prasad","c) Sardar Vallabhbhai Patel","d) Jawaharlal Nehru"),
            ("a) Venus","b) Jupiter","c) Mars","d) Saturn"),
            ("a) Rabindranath Tagore","b) Bankim Chandra Chatterjee","c) Mahatma Gandhi","d) Subhas Chandra Bose"),
            ("a) Atlantic Ocean","b) Indian Ocean","c) Arctic Ocean","d) Pacific Ocean"),
            ("a) 1942","b) 1945","c) 1947","d) 1950"))

answers = ('b','c','a','d','c')
count = 0
o=0
while(o<5):
    for idx,i in enumerate(questions):
        print(i)
        for k in options_1[idx]:
            print(k)
        print()

        guess = input("Enter the option: ")
        while guess not in ('a','b','c','d'):
            print("Enter from given option only")
            print()
            guess = input("Enter the option: ")
        if guess == answers[idx]:
            print("Correct")
            count+=1
        else:
            print("Incorrect")
        o+=1
print(f"You have Entered {count} answers correctly")