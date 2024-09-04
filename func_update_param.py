""" Situations Where the Values of
Arguments Are Updated or Not in Python"""
# Values of integers and floats are not subject to change.
a = 2
def f(x):
    x = 4
    return x

print(f(a))
print(a)

b = 3.4
print(f(b))
print(b)

# Lists
l = [1,2,3]
l2 = l
print(l)
print(l2)
l2[1] = 20
print(l2)
print(l)

def f(l):
    l[0] = "a"
    return l

print(f(l))

l = [1,2,3]
def f(x):
    x[0] = 2
    return x

def f(penguin):
    penguin[0] = 2
    return penguin

print(f(l))
print(l)

l2 = l.copy()
print(l2)
l2[0] = 10
print(l2)
print(l)

def f(x):
    l2 = x.copy()
    l2[0] = 10
    return l2

print(f(l))
print(l)