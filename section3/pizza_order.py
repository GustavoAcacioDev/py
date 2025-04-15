print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# small pizza (S): 15
# medium pizza (M): 20
# large pizza (L): 25
# add pepperoni for small pizza: 2
# add pepperoni for medium or large pizza: 3
# add cheese for any size: 1
bill = 0

if(size == "S"):
    bill += 15
elif(size == "M"):
    bill += 20
elif(size == "L"):
    bill += 25
else: 
    print("You typed the wrong input!")

if(pepperoni == "Y"):
    if(size == "S"):
        bill += 2
    else:
        bill += 3

if(extra_cheese == "Y"):
    bill += 1


print(f"The total price is: ${bill}")