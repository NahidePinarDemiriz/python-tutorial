# List Comprehension
squares = []

for i in range(1,11):
    squares.append(i*i)
print(squares)

squares = [i * i for i in range(1,11)]
print(squares)

# list compherension and functions

def cube(x):
    return x*x*x # x ** 3

cubes = [cube(x) for x in range(1,11)]
print(cubes)

# List Comprehension Using If-Else

numbers = [1,2,3,4,5,6,7,8,9]

odd_numbers = []
for e in numbers:
    if e % 2 == 1:
        odd_numbers.append(e)
print(odd_numbers)

odd_squares = [e for e in numbers if e % 2 == 1]
print(odd_squares)

# We can also implement this test logic with a function
def is_odd(x):

    if x % 2 == 0:
        return False
    if x % 2 == 1:
        return True

def is_odd1(x):

    if x % 2 == 1:
        return True
    else:
        return False

def is_odd2(x):

    if x % 2 == 0:
        return False

    return True

odd_squares = [e for e in numbers if is_odd(e)]
print(odd_squares)

def is_even(x):
    if x % 2 == 0:
        return True
    return False

odd_squares = [e for e in numbers if is_even(e)]
print(odd_squares)

weird_squares = [e if e % 2 == 0 else -1 for e in squares]
print(weird_squares)

ultra_weird_squares = [e if e % 2 == 0 else -1 for e in squares if is_even(e)]
print(ultra_weird_squares)

# Set Comprehension
numbers = [1,2,3,4,5,6,7,8,9]
set_numbers = {s for s in numbers if s in [1,2,3,4,5,6]}
print(set_numbers)

# Dictionary Comprehension
square_dict = {e: e * 2 for e in range(1, 11)}
print(square_dict)

# Nested List Comprehension
m = [[j for j in range(7)]for i in range(5)]
m = [[j for j in range(7)]for _ in range(5)]
print(m)
a = [[0,1], [20,30], [400,500]]
for l in a:
    print(l)

# Flatten - the term "flatten" refers to the process of converting multi-dimensional or nested data structures (such as lists of lists) into a single, one-dimensional list
new_m = []
for l in a:
    for e in l:
        new_m.append(e)
        print(e)
print(new_m)

flatten_m = [e for l in a for e in l]
print(flatten_m)

# only for even values
flatten_m1 = [e for l in a for e in l if e % 2 == 0]
print(flatten_m1)