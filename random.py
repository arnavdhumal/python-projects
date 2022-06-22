cost = 0.00
type_shop = input("Standard or Custom? ")

if type_shop == "Standard":
    package = input("\nPackage: ")
    if package == "Premium":
        cost += 5.99
    elif package == "Deluxe":
        cost += 18.99
    elif package == "Mad Massager":
        cost += 24.99

else:
    area = int(input("\nHow many areas? "))
    cost += area * 7.00
    time = float(input("Time (in minutes)? "))
    cost += time * 1.50

add = input("\nDid you have any Additions? Yes or No. ")

if add == "Yes":
    x = int(input("How many additions? "))
    cost += x * 1.50


print("\nYour total cost is $" + str(cost))