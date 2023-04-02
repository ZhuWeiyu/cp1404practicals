# Q1
OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, "w")
name = str(input("Enter user name: "))
print(name, file=out_file)
out_file.close()

# Q2
FILE_NAME = "name.txt"
in_file = open(FILE_NAME)
text = in_file.read().strip()
in_file.close()
print(f"Your name is {text}")

# Q3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1+number2)

# Q4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)