# Conditionals and Loops
# if else elif


# Exercise 1
age = 40

if age <= 13:
    print("Discount is UGX 1500")
elif age > 13 and age < 18:
    print("Discout is UGX 500")
elif age >= 18 and age < 65:
    print("Price is UGX 2000")
else:
    print("Senior Citizen Price is UGX 5000")


# Exercise 2
# Colors
colors = ["blue", "green", "white"]

colors_len = len(colors)
while colors_len > 0:
    print(colors[colors_len - 1])
    colors_len -= 1

user_input = input("Enter numbers 12345: ")

loop_count = len(user_input)

while loop_count > 0:
    print(user_input[loop_count - 1])
    loop_count -= 1
