# Dictionary = {key1:value1, key2:value2,...}

students_grades = {"Pinar": 70, "Gizem": 80}
print(students_grades["Pinar"])

students = {"Pinar": {"grade": 90, "student_num": 7}, "Gizem": {"grade": 70, "student_num": 6, 0: 20}}
print(students["Pinar"]["grade"])
print(students["Gizem"]["student_num"])
# dictionaries do not support indexing like lists or tuples do
print(students["Gizem"][0])

# you can change the values associated with keys using straightforward assignment or the update() method
students["Pinar"]["grade"] = students["Pinar"]["grade"] + 10
print(students["Pinar"]["grade"])

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict.update({'age': 31, 'city': 'San Francisco', 'job': 'Engineer'})
print(my_dict)

# len()
print(len(my_dict))

# Adding a new key-value pair to a Python dictionary (dict object) is straightforward
students_grades["Ali"] = 10
print(students_grades)

# del - You can use the del keyword followed by the key you want to delete from the dictionary
del students_grades["Gizem"]
print(students_grades)

# Python dictionaries , keys must be of an immutable data type
d = {(1,2):"a", (4,5): [1,2,3]}
print(d[(1,2)])

# d2= {[1,2]: 4} # List is mutable

# Empty Dict
dict = {}
dict["a"] = 1
print(dict)

print("a" in dict)


