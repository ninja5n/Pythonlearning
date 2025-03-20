a = "delhi is a clean city"

# e = a.replace("i", "z")

# print(a)


def replaceChar(string: str) -> str:
    new_string: str = str()  # just creating a empty string
    for char in string:
        if char.lower() == "i":
            new_string += "z"
        else:
            new_string += char
    return new_string


my_string: str = "delhi is a clean city"
r = replaceChar(my_string)
print(my_string)
print(r)


def replaceCHHAr(string: str) -> str:
    new_string = " "
    for char in string:
        if char.lower() == "i":
            new_string += "z"
        else:
            new_string += char
    return new_string


string = "America is a democratic country"
replaced = replaceCHHAr(string)

print(replaced)


def replaceCharr(string: str) -> str:
    new_string: str = str()
    for char in string:
        if char.lower() == "i":
            new_string += "z"
        else:
            new_string += char
    return new_string


words = "I II AM A UNITED NATIONS SUPPORTER"
erep = replaceCharr(words)
print(erep)


# replace using list

my_string: str = "America is going trailing"
new_list: list = [char if char != "i" else "z" for char in list(my_string)]
print("".join(new_list))
