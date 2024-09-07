# F-strings
x = 2
print(f"x: {x}")
print(f"x: {x+2}")

name = input("Enter your name: ")
print(f"Name: {name}")

l = [1,2,3,4]
print(f"List: {l}")

print(f"Name: {name.capitalize()}")

def square(x):
    return x*x

x = 10
print(f"The square of {x} is equal to {square(x)}")