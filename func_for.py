# Using functions as objects

# Function is applied to each element of the list, and the list is updated accordingly.
l = [1,2,3,4]

def apply(l, f):
    n = len(l)

    for i in range(n):
        l[i] = f(l[i])

def square(x):
    return x**2

apply(l, square)
print(l)

def cube(x):
    return x ** 3

apply(l, cube)
print(l)

# Applying a list of functions to a specific value
def apply_funcs(f_list, x):
    l = []
    for f in f_list:
        l.append(f(x))

    return l

print(apply_funcs([square, cube], 3))