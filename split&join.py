# split() - The split() method splits a string into a list

s = "How are you?"
print(s.split())

s = "How are you?"
print(s.split(" "))

s2 = "apple,banana,chery"
print(s2.split())
print(s2.split(","))

# join() - The join() method takes all items in an iterable and joins them into one string

l = ["lemon", "apple", "banana", "chery"]
x = ",".join(l)
print(x)

y = "-".join(l)
print(y)