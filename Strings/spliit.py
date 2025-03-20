string: str = "abc xyz pqr lmn"

# cba zyx rqp nml

my_list = string.split()  # convert string to a list # ['abc', 'xyz', 'pqr', 'lmn']
print(my_list)
# iterate over each item of list then reverse it using reverse function
# join it using join fuction
print("\n")
for items in my_list:
    new_list = list(items)
    new_list.reverse()
    new_list = "".join(new_list)
    # print new list with end to append it at new line to bring it up to one line
    print(new_list, end=" ")
