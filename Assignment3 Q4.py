names = ["Alice", "Bob", "Charlie", "David"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

with open("names.txt", "r") as file:
    for line in file:

        print(line.strip())
