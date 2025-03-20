"""
Ask user input
xyz
python is great
ryyy
until user presses "q"
then print everything

"""

# while not quit:
#     user_input = input("Enter a string: ")
# print(user_input)
# user_input = "q"
# while user_input != "q":
#     user_input = input("Enter a string: ")
#     print(user_input)


name = ""
while True:
    user_input = input("Please enter a string: ")
    if user_input == "q":
        break
    name += user_input + "\n"
print(name[:-1])
