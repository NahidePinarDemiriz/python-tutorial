# Iterating over a list
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

t = 0
for i in a:
    t += i
average = t/len(a)
print(average)

# range()
for i in range(1,4,1):
    print("Iteration", i)

for e in a:
    print(e)
    break

for i in range(len(a)):
    print(a[i])
    break
print("now")

for i in a:
    print(i)
    i = i + 10
    print(i)
    print(a)
    print("---------")
print(a)

for i in range(len(a)):
    a[i] += 10
print(a)

for i in range(len(a)):

    if i == 1:
        continue
    a[i] *= 2
print(a)

x = int(input("Which number should I check? "))

l = [2, 3, 40, 100, 10, 1]

for e in l:
    print(e)
    if e == x:
        print("Found it!")
        break
# Loop Through a Tuple

t = (1, 2, 3, 4)
for e in t:
    print(e)

a = 0
for e in t:
    a += e
print(a)

for i in range(len(t)):
    print(t[i])

# Iterate over a dictionary

d = {"student_1": [90,89], "student_2": [80,93], "student_3": [72,71]}

for k in d:
    print(k)

for k in d:
    v = d[k]
    print(v)

for v in d.values():
    print(v)

m = {"student_1": 10, "student_2": 20, "student_3": 30}

for i in m:
    value = m[i]

    if value > 20:
        print(i)

# Variable unpacking

for k,v in m.items():
    print("key:",k , "value:",v)

