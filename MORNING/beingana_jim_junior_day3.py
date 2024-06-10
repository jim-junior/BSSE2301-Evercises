# Python Best Practises

"""
Python Operators

Addition
Subtraction
Multiplication
Division
Modulus
Exponentiation
Floor division


python Bitwuse Operators

AND     &
OR      |
XOR     ^
NOT     ~


# Python Cases

1. snake_case
2. camelCase
3. PascalCase
4. UPPERCASE
5. kebab-case

"""


# Comprehensions (list, dictionary comprehensions)
# Comprehesions provide a concise way to create lists, dictionaries
# Dictionaries are used to store data values in key:value pairs. {}
# Lists are used to store multiple items in a single variable. []


# Exercise 1
# Create a list of even squares in the range of 20

even_squarres = [x**2 for x in range(20) if x % 2 == 0]

# print(even_squarres)

# Exercise 2: Create a list of tuples wgere each tuple contains a number and its cube for numbers between 1 and 10 using dictionary comprehension

cubes = [
    (k, v) for k, v in {x: x**3 for x in range(1, 11)}.items()
]
print(cubes)
