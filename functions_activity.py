
menu = {"Pizza": 2.99, "Burger": 3.99, "Hot dog": 1.99, "Cheese": 0.59, "Ice cream": 1.49, "Churro": 0.79, "Soda": 0.89}

def total_price(menu1, menu2):
    return menu[menu1]+ menu[menu2]
print(total_price("Pizza", "Burger"))

def price_difference(menu1, menu2):
    return abs((menu[menu1]- menu[menu2]))
print(price_difference("Hot dog", "Cheese"))

def inflation(menu, multiplier):
    if menu in menu:
        menu[menu]=multiplier
        return menu
    else:
        return f"{menu} is not in the menu"

