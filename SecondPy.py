Yes = "Good Job! Your answer is correct!"
No = "Oops, You're wrong. Try again."
OhNo = "Looks like it didn't work. Please answer with Yes or No. Reload to try again."
FQ = input("Do you know Python? Type Yes or No. ")
if FQ == "Yes":
    print("So you know, I'll give you some questions")
    while True:
        SQ = input("What is the word one would use to define a function? ")
        if SQ == "def":
            print(Yes)
            break
        print(No)
elif FQ == "No":
    print("That's ok. Go to https://www.w3schools.com/python/default.asp to learn the language.")
else:
    print(OhNo)
