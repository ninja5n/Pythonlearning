"""
String to replace vowels with 'z'
in aeroplane

"""


def replace_vowels(string) -> str:
    vowels = "aeiou"
    vowels = list(vowels)
    string = list(string)
    for v in vowels:
        for s in string:
            if s == v:
                string[string.index(s)] = "z"
    string = "".join(string)
    return string


replace = replace_vowels("aeroplane")
print(replace)
