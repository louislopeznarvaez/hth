cookbook =[]
def create(recipe):
    cookbook.append(recipe)
    print(f"{recipe} has been added to the cookbook")
    
def read(index):
    cookbook.index()
    if index in range (len[cookbook]):
        print(cookbook[index])
    else:
                print("sorry sir, theres not enough space in the list")

def update(index, recipe):
     if index in range(len(cookbook)):
          cookbook[index] = recipe
          print(f"recipe at index {index} has been updated to {recipe}") 
     else:
           print("index out of range, try again")

def  destroy(index):
     if index in range(len(cookbook)):
            recipe = cookbook.pop(index)
            print(f"{recipe} now has been deleted from the cookbook")
     else:
           print("index out of range, try again")

def list_all_recipes ():
      if cookbook:
            print("all recipes in the cookbook:")
            for index, recipe in enumerate(cookbook):
                  print(f"{index}: {recipe}")
      else:
            print("No recipes in the cookbook.")

def main():
    while True:
        print("\nCookbook Recipes")
        print("1. Add a Recipe")
        print("2. Read a Recipe")
        print("3. Update a Recipe")
        print("4. Delete a Recipe")
        print("5. Display all Recipes")
        print("6. Exit")


        choice = input("Choose an option (1-6): ")


        if choice == "1":
            recipe = input("Enter the name of the recipe: ")
            create(recipe)
        elif choice == "2":
            index = input("Enter the index of the recipe to read: ")
            index = int(index)
            read(index)
        elif choice == "3":
            index = input("Enter the index of the recipe to update: ")
            recipe = input("Enter the name of the recipe you want to update it with: ")
            index = int(index)
            update(index, recipe)
        elif choice == "4":
            index = input("Enter the index of the recipe to delete: ")
            index = int(index)
            destroy(index)
        elif choice == "5":
            list_all_recipes()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")


main()


