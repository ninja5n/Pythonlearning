try:
    my_list = [34, 55, 64, 24, 242.1, 133]
    print(f"Element at index 0 = {my_list[0]/0}")
except ZeroDivisionError as z:
    # runs when issue happens
    print(ZeroDivisionError.__name__)
    print(z)
    print("There was a error!")
else:
    # runs when no issues
    print("There were no issues!")
finally:
    # some task you want to always perform
    # such as disconnecting from a database
    # disconnecting a ssh session
    print("The is a final step which runs irrespective of success or fail code.")
    print(my_list)
