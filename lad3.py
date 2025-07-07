#lad3

#task 1: working with strings
food = "wingstop"
print(food[0:3])
print(food[-3:8])
first_last= food[0]+ food[-1]
print(first_last)
food_list= food.split()
print(food_list)
joined_food = "  ".join(food_list)
print(joined_food)

#task 2 working with lists
number_list = [1, 7675647456, 32, -5, 0, 234]
number_list.append(67)
print(number_list)
number_list.insert(3, 1000)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)
print(number_list[0:3])
print(number_list[-3:])
first_last= number_list[0] + number_list[-1]
print(first_last)

#task 3 working with keys and values
books= {"kazu kibuishi":"amulet", "michelle zauner":"H mart", "tommy orange":"there there", "angie thomas":"the hate u give"}
print(books.keys())
print(books.values())
print(books.get("michelle zauner"))
books.pop("tommy orange")
print(books)
del books["kazu kibuishi"]
print(books)