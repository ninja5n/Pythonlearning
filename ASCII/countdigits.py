a = "Pyth10n us A Gre3AT La1ngAU3343434584GE"


# find largest and second largest number in a string
largest = 0
second_largest = 0
for char in a:
    if char.isnumeric():
        if int(char) > largest:
            largest = int(char)

for char in a:
    if char.isnumeric():
        if int(char) > second_largest and int(char) < largest:
            second_largest = int(char)

print("Largest number is: ", largest)
print("Second largest number is: ", second_largest)
