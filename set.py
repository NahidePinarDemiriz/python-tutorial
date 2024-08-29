# Set
s = {1, 2, 3, 4, 5, 1}
print(s)

a = {}
print(type(a)) # It is a dict

b = set()
print(type(b)) # It is a set

l = [1, 2, 3]
print(set(l))

t = (1, 2, 3, 3, 4)
print(set(t))

# Set counts whitespace characters and is unordered
message = "Hello there!"
set1 = set(message)
print(set)

# len()
print(len(set1))

# it does not support indexing like lists or tuples

#print(set[0])

# add() used to add a single element to an existing set
l = {1, 2, 3}
l.add(4)
print(l)

# remove() method is used to remove a specific element from the set
l.remove(3)
print(l)

# discard() - does not raise an error if the element is not found in the set
l.discard(3)
print(l)

# Difference [s1-s2 and s1/s2]
s1 = set([1, 5, 10])
s2 = set([2, 5, 3])

print(s1.difference(s2))
print(s2.difference(s1))

# Symmetric Difference -> (s1-s2) u (s2-s1)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))

# Intersection -> s1&s2
print(s1.intersection(s2))
print(s1&s2)
print(s1-(s1-s2))

s1.intersection_update(s2)
print(s1) # s1 updated

# Union
s1 = set([1, 5, 10])
print(s1.union(s2))

# Disjoint Sets - refer to sets that have no elements in common
print(s1.isdisjoint(s2))
s3 = set([9, 11])
print(s1.isdisjoint(s3))
print(len(s1.intersection(s3)) == 0)

# issubset() method is used to check if one set is a subset of another set
s4 = set([1, 10])
print(s4.issubset(s1))

# issuperset() is used to check if a set contains all elements of another set
print(s1.issuperset(s4))










