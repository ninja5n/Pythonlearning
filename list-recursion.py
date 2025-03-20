# List Recursion function


def recursive_sum(lst):
    if not lst:  # Base case: empty list
        return 0
    return lst[0] + recursive_sum(lst[1:])  # Recursive case


# Example usage
numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))  # Output: 15
# In this example, the recursive_sum function calculates the sum of a list of numbers using recursion.
# The function has two cases:
# Base case: If the list is empty, the function returns 0.
# Recursive case: The function adds the first element of the list to the sum of the rest of the list (excluding the first element).
# This process continues until the base case is reached, resulting in the sum of all elements in the list.
# The example usage demonstrates how to calculate the sum of a list of numbers using the recursive_sum function.
# The output of the example is 15, which is the sum of the numbers 1, 2, 3, 4, and 5.
# List recursion is a powerful technique for solving problems that involve processing lists or sequences of data.
# By breaking down a problem into smaller subproblems and combining the results, recursion can be used to perform complex operations on lists efficiently.

# print(numbers[0] + numbers[1:])
print(numbers[0])
print(type(numbers[0]))
