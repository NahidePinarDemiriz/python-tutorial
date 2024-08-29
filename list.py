# List
student_grades = [10, 20, 30, 40, 50]
a = ["a", "b", "c", "d", "e"]
b = [True,False]
c = [[1,2], [3,4], [5,6]]

# Lists can contain different types of data
d = [1, "hello", 3.14, True, [1, 2, 3]]

# Indexing and Slicing
print(student_grades[0])
print(student_grades[-1])
print(student_grades[1:])
print(student_grades[1:3])
print(student_grades[:100])

# Lists are mutable
student_grades[0] +=5
print(student_grades)
l = [0, 1, 2, 3]
print(l)
l[0:3] = 0, 10
print(l)

# Slicing must be done with iterables; it cannot be done with a single value
# l[0:3] = 10 # can only assign an iterable
l[0:3] = [30]
print(l)

# len() - returns the number of elements in a string
print(len(l))

# append - to add a single element to the end of the list
p = [1, 2, 3]
print(p)
p.append(4)
print(p)

# extend() - to add multiple elements from an iterable (like another list, tuple, or set) to the end of the list.
s = [1, 2, 3]
print(s)
s.extend([4, 5, 6])
print(s)
s.extend("hello")
print(s)

# insert() - to add a single element to a list at a specific index
k = [0, 1, 2, 3]
k.insert(2, 4)
print(k)

# remove() - o remove the first occurrence of a specified value from a list
k.remove(0)
print(k)
try:
    k.remove(40)
except ValueError:
    pass
# remove() removes the first encountered element
m = [0, 1, 2, 3, 4, 3]
m.remove(3)
print(m)

# pop() - method is used with lists and dictionaries to remove and return an item
print(m.pop(0))
print(m)

print(m.pop(0) + 1)
print(m)

# count() -  method is used to count the number of occurrences of a specified value within a list or a string
h = [0, 1, 2, 3, 3]
print(h.count(3))

# Aliasing - refers to the concept where two or more variables refer to the same object in memory
a = 2
b = a
print(b)
a = a + 1
print(a)
print(b)

# for lists
list1 = [0, 1, 2, 3, 4]
list2 = list1
print(list1)
print(list2)
list1[0] = 100
print(list1)
print(list2)

list3 =[0, 1, 2, 3, 4]
list4 = list3.copy()
print(list3)
print(list4)
list3[0] = 100
print(list3)
print(list4)

# List concatenation - using the '+' operator
l1 = [0, 1, 2, 3, 4]
l2 = [5, 6, 7, 8, 9]
print(l1+l2)

# Using the index() Method
array = [1, 2, 3, 4, 5]
print(array.index(3))

# reverse() - the process of reversing the order of elements in a list - inplace
array.reverse()
print(array)
# The difference is that inplace operations modify the original data structure, while not
# inplace operations create a new copy without altering the original.
print(array[::-1]) # not in-place
print(array)

# sorted() function is used to return a new list containing all items from the iterable in ascending order
example = [2, 4, 1, -1]
print(sorted(example)) # not inplace
print(example)

example.sort() # inplace
print(example)

mixed_list = ["3", "a", "1", "c", "4", "b", "2", "d"]
mixed_list.sort()
print(mixed_list)







