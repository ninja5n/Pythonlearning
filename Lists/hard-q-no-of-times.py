my_list = [1, 2, 3, 4, 5, 5, 5, 10, 19, 19, 19]

# create a unique list from the given list
unique_list = list(set(my_list))


# print the number of times each element occurs in the list
for item in unique_list:
    print(f"{item} occurs {my_list.count(item)} times.")


my_list = []
# print the number that occurs the most times without using list comprehension
max_count = 0
most_occuring = None
for item in unique_list:
    count = my_list.count(item)
    if count > max_count:
        max_count = count
        most_occuring = item
print(
    f"\nThe number that occurs the most times is {most_occuring} with {max_count} occurrences."
)


# max_count = max([my_list.count(item) for item in unique_list])
# most_occuring = [item for item in unique_list if my_list.count(item) == max_count]
# print(
#     f"\nThe number that occurs the most times is {most_occuring[0]} with {max_count} occurrences."
# )
