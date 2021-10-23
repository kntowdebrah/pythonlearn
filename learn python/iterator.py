# tuples are definitely iterable
mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# strings are definitely also iterable.
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


mystr = "banana"

for x in mystr:
    print(x)
