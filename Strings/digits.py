"""
Enter a = python
Enter b = good

then output == pythongood

If

Enter a = 50
Enter b = 20

70
"""

a = input("Enter a: ")
b = input("Enter b: ")

if a.isalpha() and b.isalpha():
    c = a + b
elif a.isdigit and b.isdigit():
    c = int(a) + int(b)
print(c)
