for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=" ")

# b.
for i in range(20, 0, -1):
    print(i, end=" ")

# c.
stars = int(input("Enter number of stars: "))
for i in range(stars):
    print("*", end="")

# d.
stars = int(input("Enter number of stars: "))
for i in range(1, stars + 1):
    print("*" * i)
print()