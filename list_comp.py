# List Comprehension
# used to create a list
# Syntax: [expression for item in iterable if condition]

# Example 1
# Create a list of squares of numbers from 1 to 10
squares = [i**2 for i in range(1, 11)]
print(squares)

my_list = [i for i in range(1, 11)]
print(my_list)

# Example 2
# Create a list of even numbers from 1 to 10
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

# Example 3
# create a list of 1 and 0 alternatively
ones_zeros = [i % 2 for i in range(1, 11)]
print(ones_zeros)

# Example 4
# create a kust if range with negative numbers using step and slice
negative_numbers = [i for i in range(0, -11, -4)]
print(negative_numbers)

# Example 5
# create a list comprehension with if else
# if the number is even, square it, else cube it
even_odd = [i**2 if i % 2 == 0 else i**3 for i in range(1, 11)]
print(even_odd)


# Example 6
# create a list comprehension with nested list
nested_list = [[i for i in range(1, 4)] for j in range(3)]


# Example 7
print("\nExample 7\n")
my_list = [i for i in range(1, 51) if i % 5 == 0 or i % 4 == 0]
print(my_list)


# Example 8
print("\nExample 8\n")


# create a list using list comprehension with functions
def square(x):
    return x**2


def cube(x):
    return x**3


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


functions = [square, cube, factorial]
my_list = [f(5) for f in functions]  # [25, 125, 120]
print(my_list)
