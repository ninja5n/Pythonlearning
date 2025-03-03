tup = (32, 45, 100, 67, 77, 43)

print(tup.count(32))  # 1
print(tup.index(100))  # 2
print(tup.index(77))  # 4

# Membership operator (in, not in)
print("ninad" in tup)  # False
print("ninad" not in tup)


# comprehension
tup = (i for i in range(10))
print(tup)  # <generator object <genexpr> at 0x7f1b4c6b8d60>
print(tuple(tup))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# Tuple unpacking
tup = (1, 2, 3)
a, b, c = tup
print(a, b, c)  # 1 2 3

# Swapping
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10

# Tuple as key in dictionary
d = {(1, 2): "Ninad"}
print(d[(1, 2)])  # Ninad
d = {tup: "Ninad"}
print(d[tup])  # Ninad

# Tuple as value in dictionary
d = {1: (1, 2, 3)}
print(d[1])  # (1, 2, 3)
d = {1: tup}
print(d[1])  # (1, 2, 3)

# Tuple as key in set
s = {(1, 2, 3)}
print(s)  # {(1, 2, 3)}
s = {tup}
print(s)  # {(1, 2, 3)}
