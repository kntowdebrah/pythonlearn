import os
file = open(
    "\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt")

print(file.read())

# reading parts of the document
file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt", "r")

print(file.read(5))


# read lines from a file
file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt", "r")

print(file.readline())
print(file.readline())

# using a loop to read file content
file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt", "r")

for x in file:
    print(x)

file.close()  # closes the file.


# writing to a file
file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt", "a")

file.write("Now the file has more content")
file.close()

file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt", "r")

print(file.read())

# overwriting the content of a file
file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt", "w")

file.write("Woops! I have deleted the content!")
file.close()

# open and read the file after the appending:
file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\learn python\\demofile.txt", "r")
print(file.read())


# creating a new file 'to write mulitple lines at \n'
file = open("mynewfile0.txt", "x")
file.write("I am trying out my own file. I am loving it\n")
file.write("I hope this second line write on it.")
file.close()

file = open("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\mynewfile0.txt", "r")
print(file.read())

# deleting a file

os.remove("\\Users\\kdebrah\\OneDrive\\Documents\\GitHub\\pythonlearn\\mynewfile0.txt")

# checking if path exist before deleting
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")


# removing folders
os.rmdir("myfolder")
