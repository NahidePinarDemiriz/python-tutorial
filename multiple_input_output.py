# Multiple Input
def power (x,y):

    return x ** y

print(power(2,3))

# Functions returning multiple values
def f(x):
    return 2*x, 10*x

print(f(10)) # Returned as an output tuple

"""Just like in variable unpacking, we can assign 
these two values to different variables."""
a, b = f(10)
print(a)
print(b)

# Multiple inputs and outputs
def func(x,y):
    return 2*x*y, 10*x*y

print(func(10, 2))