# Variable Unpacking
x, y = (4, 7)
print(x)
print(y)

x, y, z = (4, 7, 8)
print(x, y, z)

# If we are not going to use some values, we can write it like this
x, _ = (5, 10)
print(x)

# Using * will assign the remaining elements to z
x, y, *z = (10, 20, 30, 40, 50)
print(x)
print(y)
print(z)
print(type(z))

x, y, *_ = (10, 20, 30, 40, 50)
print(x)
print(y)

x, y, *z, t = (10, 20, 30, 40, 50)
print(x)
print(y)
print(z)
print(t)

x, y, *z, t = (10, 20, 30, 40)
print(x)
print(y)
print(z) # z will return as a list even if it contains a single value
print(type(z))
print(t)

# It will give an error
x, *y, *z = (1, 2, 3, 4, 5)