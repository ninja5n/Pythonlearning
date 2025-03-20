mylist = [1, 2, 3, 4, 5, 5, 10, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = input("Enter start index: ")
j = input("Enter end index: ")
z = input("Enter step size: ")

if z:
    print(mylist[int(i) : int(j) : int(z)])
else:
    print(mylist[int(i) : int(j)])
