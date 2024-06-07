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
