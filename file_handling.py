# f = open("example.txt", 'r')

# read_file = open('example.txt', 'r')
# human_readable = read_file.read()
# print(f"Data in read_file: {read_file}")
# print(f"Data type of read_file: ", type(read_file))
# print("\nData in human_readable:\n", human_readable)
# print("Data type of human_readable: ", type(human_readable))

# read_file.close()

# fruits = ["apple", "banana"]
# fruits.append("mango")
# print(fruits[2])

# creating txt file
file = open("data.txt", "w")
file.write("Hello, Pranish this side.")
file.close()
print("file created")

# reading the file
file = open("data.txt", "r")
print(file.read())
file.close()

# updating or append
file = open("data.txt", "a")
file.write("\nHello this is the updating text.")
file.close()
print("File Updated!")

import os
os.remove("data.txt")
print("File deleted!!!")