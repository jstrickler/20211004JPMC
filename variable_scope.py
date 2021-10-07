
x = 100  # global variable (global to file)

def spam():
    animal = "wombat"  # local variable
    print("in spam(): x is", x)

spam()
# print(animal)
print(x)

