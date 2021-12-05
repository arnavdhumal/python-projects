Yes = "Good Job! Your answer is correct!"
OhNo = "Looks like it didn't work. Reload to try again."
FQ = input("Do you know Python? Type Yes or No. ")


if FQ == "Yes":
    print("So you know, I'll give you some questions")
    SQ = input("What is the word one would use to define a function? ")
    if SQ == "def":
        print(Yes)
        
elif FQ == "No":
    print("That is ok. Go to https://www.w3schools.com/python/default.asp to learn the language.")
else:
    print(OhNo)
