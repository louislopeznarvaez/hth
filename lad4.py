#lad4.py

#task 1
checking = "yes"

while checking == "yes":
    print("what is your age")
    user_input = input()
    
    if int(user_input) >= 18:
        print("yes you can vote")
    else:
        print("you can't vote")
        print("would you like to check another age?")
        user_input2 = input()
        checking = user_input2
        

#task 2
numbers = [15, -7, 0, 23, -42, 8]
for number in numbers:
    if number > 0:
        print( f"{number} is positive")
    elif number < 0:
        print( f"{number} is negative")
    else:
        print( f"{number} is zero")

#task 3
inventory="coal", "dirt", "gold", "gravel",  "iron", "emerald"
for block in inventory:
    print(f"{block} is in the inventory")
    if block == "emerald":
        print("jackpot! you found an emerald!")
