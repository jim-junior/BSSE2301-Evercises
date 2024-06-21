
# Exampkle 3: Write a file and read a file

# Writing to a text file

import xml.etree.ElementTree as ET
import json
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

import csv

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
