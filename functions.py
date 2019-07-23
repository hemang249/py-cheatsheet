# Working with User Defined Functions in Python 3

# Defining a Function
def greet():
    print("Hello User")

greet()

# Passing Arguments To a Function
def sayHello(username):
    print("Hello " + username)

sayHello("Hemang")

# Keyword Parameters
def pet(breed , name):
    print("I have a " + breed + ". His Name is " + name)

pet(breed = "Labrador" , name = "Cooper")


# Default parameters 
def food(type = "Pizza"):
    print("I'll have a " + type)

food()

# Returning Values From A Function
def sum(x , y):
    return (x+y)

num1 = 5
num2 = 6
num3 = sum(num1 , num2)
print(num3)

# Optional Arguments
def nameprint(fname , lname = ""):
    print(fname + lname)

nameprint("Hemang")

# Lists and Functions
def listappend(mylist):
    mylist.append("Hemang")

xlist = ["Sam" , "Mark"]
listappend(xlist)
print(xlist)

# Passing Arbitrary number of Arguments
def pizza(*toppings):
    for topping in toppings:
        print(topping)

pizza('Pepperoni', 'Capsicum', 'Mushrooms')