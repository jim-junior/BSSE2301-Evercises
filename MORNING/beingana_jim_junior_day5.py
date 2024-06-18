# FUNCTIONS


def get_coordinates():
    return 10, 20


x, y = get_coordinates()
print(x, y)

# Exercise 1: Define a function `greet` with a parameter `name` , set to 'guest', and print a message: I am a software programmer


def greet(name='guest'):
    print("Hello, " + name + "! I am a software programmer.")


greet()
greet('Beingana')

# Example 3 :Return multiple return values


def get_name_and_position():
    name = 'Beingana Jim Junior'
    position = 'I am a Software Programer'
    return name, position


name, position = get_name_and_position()  # Unpack the tuple correctly
print(name, position)

# Exercise 4: Return multiple return values of your name and age


def personal_info():
    name = 'Beingana Jim Junior'
    age = 20
    return name, age


name, age = personal_info()
print(name, age)


# Notes
"""_summary_
def : Keyword to defibe a function
function_namr: Name of the function
parameters: Optional,arguments passed t the function 
Docstrings: Optional, describes the dunction purpose
return: Optional, returns a value from the function
    """

# syntax for defining a function
# def function_name(parameters):
#     """Docstrings"""
#     function body
#     return value

# Lambda functions
# they are small anonymous functions defined using the lambda keyword.\
# They are restricted to a single expression

# Syntax for lambda function
# lambda parameter : Expression

# A lambda function to add two numbers


def add(a, b): return a + b


print(add(45, 70))

# Example 6: Use cases of lambda function for sorting
coordinates = [(1, 2), (2, 3), (3, 1), (5, 0)]

# Sort the coordinates based on the second element of the tuple
coordinates.sort(key=lambda x: x[1])

print(coordinates)


# Example 6: Get the squares of 1 and 5 using map, filter and reduce

number_squares = [1, 2, 3, 4, 5]

# Using map
number_squares = list(map(lambda x: x**2, number_squares))

print(number_squares)

# Using filter
number_squares = list(filter(lambda x: x in [1, 5], number_squares))


print(number_squares)

# Exercise 4 : Define a function to get user info that accepts arbitrary keyword arguments and print each
# key value pair


def get_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


get_user_info(first_name="Beingana", last_name="Jim Junior",
              age=20, email="jimjunior854@gmail.com", gender="Male")
