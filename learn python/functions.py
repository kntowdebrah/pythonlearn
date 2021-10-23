def my_function():
    print("Hello from a function")


my_function()

# passing arguments


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

# passing tuple unknown number


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")

# the order of the argument doesn't matter keywaord argument


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# when we do not know the number of keyword argument that will be passed
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# default parameter function
def my_function(country="Norway"):
    print("I am from  " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# passing a list as an argument


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# a function returns a value
def my_function(x):
    return 5*x


print(my_function(3))
print(my_function(6))

# recursion function


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")

tri_recursion(6)
