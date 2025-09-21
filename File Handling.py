# Opening and Reading a File
f = open("demo.txt", "r")
print(f.read())
f.close()


# Writing to a File
f = open("demo.txt", "w")
f.write("Hello Python World!")
f.close()


# Appending to a File
f = open("demo.txt", "a")
f.write("\nThis is new line.")
f.close()


# Reading Line by Line
f = open("demo.txt", "r")
for line in f:
    print(line)
f.close()