# Classes and basic OOP principles In Python3

# Creating Classes and their instances
class Pet():
    
    def __init__ (self ,name , breed , age):
        self.name = name
        self.breed = breed
        self.age = age
        print('I have a ' + self.breed + ', his name is ' + self.name + ' and He is ' + self.age +' years old')

    def food( self , foodtype):
        print(self.name + " eats " + foodtype)

my_pet = Pet('Cooper', 'Labrador', '1')
my_pet.food('Pedigree')

# Settig default attribute values
class User():

    def __init__(self , name , email , age):
        self.name = name
        self.email = email
        self.age = age
        self.date_of_birth = "NULL"

    def print_info(self):
        print("Name : " + self.name)
        print("Email : " + self.email)
        print("Age : " + str(self.age))
        print("Date of Birth : " + self.date_of_birth)        

myUser = User('Hemang', 'hemang@example.com', 18)
myUser.print_info()

# Inheritance in Pyhthon 3

class Animals():

    def __init__(self , species , name):
        self.species = species
        self.name = name
    

class Dog(Animals):

    def __init__(self , species , name):
        super().__init__(species , name)

    def print_info():
        print("Species : " + self.species + " Name : " + self.name)

my_Dog = Dog("Labrador" , "Cooper")
