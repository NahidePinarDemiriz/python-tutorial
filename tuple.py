# Tuples are immutable
x = 10
y = 30
location = (x,y)
print(location)

# Indexing and slicing
print(location[0])
print(location[:])

t = ([1, 2, 3], 2, (1,2))
print(t[0][0])
t[0][0] = 23
print(t[0][0])

a = 1, 2, 3, 4
print(type(a))
