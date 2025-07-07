# lad5

# task 1

def cat_greeting(word):
    print(f'cat says {word}')

cat_greeting("meow")

# task 2
def generate_superhero_power():
    name = "louis" 
    power= "super speed"
    print(f'{name} has the power of {power}')

generate_superhero_power()

# task 3
def generate_superhero_power1():
    power="teleportation"
    return power

print(generate_superhero_power1())

# task 4
def generate_superhero_powrer2(user_name, super_power):
    message= user_name + " has the power of " + super_power + "!"
    return message

print(generate_superhero_powrer2("louis","mind control"))

# task 5
def cat_greeting_loop(greeting):
    for i in range(5):
        print(f'the cat says {greeting}')

cat_greeting_loop("meow")

# task 6
def generate_multiple_powers(powers):
    for i in powers:
        print(i)
       
powers = ["super healing","super huamn strength","transformation"]
generate_multiple_powers(powers)
