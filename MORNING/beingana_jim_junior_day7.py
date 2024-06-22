
import csv
import json
import xml.etree.ElementTree as ET

# Inheritance and polymorphism

"""_summary
    Inheritance and method overriding
    polymorphism and method resolution order
    Abstract classes and interfaces
"""
# Inheritance and method overriding
"""_summary
    --description
    Inheritance and method overriding allows a class(child class)to inherit attributes and methods from another class(parent class)
    Key concepts
    Base class (parent class): Class whose properties are inherited by another class.
    Derived class (child class): Class that inherits attributes and properties from another base class.

"""
# Example 1:Syntax create a class where a dod inherits from animal and overrides with the speak method


# polymorphism
# polymorphism allows objects of different classes to be treated as objects of a common super class.
# Method resolution order (MRO) is order in which python looks for a method in a hierarchy classes.
#  #Example 2:How polymorphism works in python


class Animal:
    """Animal"""

    def speak(self):
        return "Crock"


class Dog(Animal):
    def speak(self):
        return "Barks"


class Cat(Animal):
    def speak(self):
        return "Meow"


def make_animal_speak(animal):
    print(animal.speak())


make_animal_speak(Dog())
make_animal_speak(Cat())


# Exercise 1:Create a simple application to manage different types of vehicles , Implement
# Derived class to demonstrate inheritance and polymorphism
"""summary
    Requirements
    1 baseclass to vehicles
    Attributes:make,model and year Methods:display_info()
    2,Derived classes
    car:inherit from vehicle
    attributes: number_of_doors
    overrides: display_info()
    Motorcycle:inherits from vehicle
    Attribute,type_of_bike(cruiser,sport,touring)
    #Exercise 2:
    create a function that accepts a list of vehicles and call their display_info()method to print details of each vehicle
    
"""


class Vehicle:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")


class Car(Vehicle):

    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.number_of_doors}")


class Motorcycle(Vehicle):

    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of Bike: {self.type_of_bike}")

# Exercise 2


def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print()  # For better readability


# Example usage:
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Yamaha", "YZF-R3", 2021, "Sport")

vehiclearr = [car, motorcycle]
display_vehicle_info(vehiclearr)


# Reading and writing files in python
"""
    summary
    1. working with text files
    handling CSV files
    JSON and XML files processing
    """
# 1. working with text files ,open,read,write and close
# note:python provides inbuilt functions to handle text files.
# key concepts
"""
    summary
    description
    opening file:open() function (r,w,a,r+)
    reading file: read() function
    writing file:write() function
    close file:close() function
    """
# example 3: write a file and read a file
# writing to a text file
with open('jeff.txt', 'w') as file:
    file.write('iam jeff Geoff and i love python.\n')
    file.write('i used python for automation')

    # reading from a text file
with open('jeff.txt', 'r') as file:
    content = file.read()
    print(content)

    # handling CSV files
    """
    summary
    CSV  (comma separated values)file widely for data exchange.
    key concepts:
    reading CSV file:using 'CSV.reader()'
    writing CSV files:Using 'CSV.Writer'
    DictReader and DictWriter: the class read and write CSV files as dictionaries
    """
# Exampkle 3: Write a file and read a file

# Writing to a text file

with open('data.txt', 'w') as file:
    file.write('i am Jeff Goef and I use python python\n')
    file.write('This is our new text file\n')
    file.write('and this is another line.\n')
    file.write('Why? Because we can.\n')


# Handling CSV files

"""
CSV (Comma Separated Values) file widely for data exchange


Key Concepts:
Reading CSV files: Using 'csv.reader()'
Writing CSV files: Using 'csv.writer()'
DictReader and DictWriter: The class read and write CSV files as dictionaries

"""

# Example 4: Wrriting and Reading CSV files


# Writing to CSV files

with open('data.csv', "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "position", "course"])
    writer.writerow(["Jeff Geoff", "Lecturer", "BSE"])
    writer.writerow(["Jim Junior", "Student", "BSE"])

# Read from a CSV file

with open("jeff.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# JSON and XML file processing
"""
JSON ( Javascript object Notation) and XML (eXtensible Markup Language) are formats used to structure data.

Key Concepts:
Loading JSON Data: using 
Parsing JSON Data: using json.loads() for handling JSON strings

"""

# Example 6: Write and read JSON file

# writing to a JSON file

student_data = {
    "name": "ahaabwe",
    "course": "BSE",
    "year": "Year2"
}

# Opeb the file

with open("student_data.json", "w") as json_file:
    json.dump(student_data, json_file)

# Reading the JSON file
with open("student_data.json", "r") as json_file:
    student_data = json.load(json_file)
    print(student_data)

# Exercise 2: Write and read XML file

# WRITING TO AN XML FILE


# Create the root element
root = ET.Element("root_tag")

# Add child elements
sub_element = ET.SubElement(root, "sub_tag")
sub_element.text = "data"

# Add attributes
sub_element.set("attribute_name", "value")

# Write the XML tree to a file
tree = ET.ElementTree(root)
tree.write("data.xml")

# READING FROM AN XML FILE
tree = ET.parse("data.xml")

# Get the root element
root = tree.getroot()

# Access elements by tag name
elements = root.findall("tag_name")

# Access element attributes
attribute_value = elements[0].attrib["attribute_name"]

# Loop through child elements
for child in elements[0]:
    print(child.tag, child.text)


# Exercise 3: Using Abstraction calculate the area and perimeter of a rectangle


class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__length * self.__width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.__length + self.__width)


rectangle = Rectangle(5, 3)

area = rectangle.area()
perimeter = rectangle.perimeter()

print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
