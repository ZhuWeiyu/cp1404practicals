# 1.
out_file = open("name.txt", 'w')
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close()

# 3.
total = 0
with open("numbers.txt", 'r') as in_file:
    # read first two numbers
    for i in range(2):
        number = int(in_file.readline())
        total += number
print(total)

# 4.
total = 0
with open("numbers.txt", 'r') as in_file:
    # read all the lines
    for line in in_file:
        total += int(line)
print(total)