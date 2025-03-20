# zip function in python

list1 = [1, 2, 3, 4, 5]
list2 = ["one", "two", "three", "four", "five"]

zipped = zip(list1, list2)
print(zipped)

# Convert the zip object to a list
zipped_list = list(zipped)
print(zipped_list)

# Unzip the zipped list
unzipped = zip(*zipped_list)
unzipped_list1, unzipped_list2 = list(unzipped)
print(unzipped_list1)
print(unzipped_list2)
