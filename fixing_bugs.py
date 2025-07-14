# task 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])
# i just remove 1 so i can see the numbers correctly

# task 3
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))
# i added a colon : to the radius

# task 4
def is_even(number):
   if number % 2 == 0: #its was missing a colon
      return True
   else:
      return False
 
print(is_even(4))
print(is_even(7))

# taks 5
for i in range(5):
  print(i)
#missing a colon

# task 6
def greet(name):
   return "Hello, "  + name

print(greet("Alice"))
# it was missing a plus

# task 7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
	sum += number
print("Sum of numbers:", sum)
# had to add a psace so the sum can go in to the middle

# task 8
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1) #had to remove the plus then i added a mynus
 
print(factorial(5))

# task 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":  #i added a equal sign
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# task 10
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2 #you cannt divide by 0 so i changed the number to 2
print(divide_numbers(num1, num2))
