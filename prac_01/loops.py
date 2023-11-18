for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_star = int(input("Number of stars:"))
while number_of_star < 0:
    print("Invalid number.")
    number_of_star = int(input("Number of stars:"))
else:
    for i in range(number_of_star):
        print("*", end="")
    print()

x = 0
number_of_star = int(input("Number of stars:"))
for i in range(number_of_star):
    x += 1
    print(x * "*")
