try:
    print(x)
except:
    print("An exception occurred")


try:
    print(X)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")

try:
    f = open("demoFile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went ")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


print("")
print("")
print("")

x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")


x = "hello"

if not type(x) is int:
    raise Exception("Only integers are allowed")

x = "hello"

if not type(x) is int:
    raise Exception("Only integers are allowed")
