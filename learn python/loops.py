## while loop ##
i = 1
while i < 6:
    print(i)
    i += 1

print(" ")
print(" ")
# using break inside a while loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# using continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

    # using an else in
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

   # for loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# looping through a string
for x in "banana":
    print(x)

# looping through an list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# using the range function
for x in range(6):
    print(x)


# using a proper range
for x in range(2, 6):
    print(x)


# using range with increment value
for x in range(2, 30, 3):
    print(x)

# using an else in a for loops
for x in range(6):
    print(x)
else:
    print("Finally finished!!")

# nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# using the pass statement
for x in [0, 1, 2]:
    pass
