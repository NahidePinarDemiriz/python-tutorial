# Writing comments for functions
import inspect
def square(x):
    """
    Returns the square of a number.

    Parameters:
    x (int or float): The number to be squared.

    Returns:
    int or float: The square of the input number.
    """
    res = x * x
    return res

print(square(3))

help(square) # Docstring
print(inspect.getdoc(square))  # Docstring
print(inspect.getsource(square))  # Body