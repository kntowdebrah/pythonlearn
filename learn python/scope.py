def myfunc():
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)


def myfunc():
    global x
    x = 300

myfunc()

print(x)
