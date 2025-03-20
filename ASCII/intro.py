a = "PythOn is A Great Language"

count = 0

for char in a:
    ascii_number = ord(char)
    if ascii_number >= 65 and ascii_number <= 90:
        count += 1

print(count)
