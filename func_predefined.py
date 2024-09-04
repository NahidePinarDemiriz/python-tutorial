# Predefined Parameters
def hello(end, start = "Hello"):
    print(start + " " + end)

hello("Denis")
hello("Denis", start="Hey")

def power(x, y=1):

    return x ** y
print(power(3))
print(power(3, y=2))
