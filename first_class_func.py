# First Class Function

def square(x):
    return x*x

a = square
print(a(2))

"""" In Python, functions are treated as first-class objects, 
which means you can pass them as arguments to other functions."""

def f2(x,f):
    return f(x) + 4

print(f2(3, square))

def f3(x):
    return x**5

print(f2(2,f3))