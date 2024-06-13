# Dictionaries
"""_summary_
Dictionaries in python are collections of keys and values 
-Unordered
-Mutable and 
-indexed by keys

"""
# Example 1
# create a dictionary for a student persuing software engineering
# the key must be your name , age , technology interest ,course and year of study
# put your own details

student_dict = {
    'name': 'Beingana Jim Junior',
    'age': '20',
    'technology': 'AI',
    'course': 'BSSE',
    'year': 'Year 3'
}

print(student_dict['year'])

# Access values

# Modify values
# Exercise 1: Modify age and technology
student_dict['age'] = 25
print(student_dict['age'])
student_dict['technology'] = "Web Development"
print(student_dict['technology'])

# Example2: Adding keys and values
student_dict['email'] = 'jimjunior854@gmail.com'
print(student_dict['email'])

# Exercise 2 : remove key and value from tha dictionary
del student_dict['age']
print(student_dict)


# Exercise 3: Use the update method to update to change the value  in age
student_dict.update({'age': '25'})
print(student_dict)

# Exercise 4: Use the if check t chrck if the age is present in the dictionary
if 'age' in student_dict:
    print("age is present in the dictionary: ", student_dict['age'])

else:
    print("age is not present in the dictionary")


# Exercise 5 : Use the update method to change the course and add a new key like ' whatsapp number to the dictioanry'
student_dict = {
    'name': 'Beingana',
    'age': '23',
    'year': 'Year3',
    'technology': 'ML',
    'course': 'BSSE',
}
student_dict.update({'course': 'CSC', 'WhatsApp': '0704203035'})
# print the updated dictionary
print(student_dict)
