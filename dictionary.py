# Dictionaries and common Dictionary Operations used in Python 3

# Declaring a Dictionary
    # dictionary = {'key' : 'value'}
myInfo = {
    'name' : 'Hemang', 
    'age' : '18', 
    'Hobby' : 'Programming'
    }

print(myInfo)
print( 'My name is '  + myInfo['name'])


# Creating new key-value pairs
    # dictionary['key'] = value
myInfo['Height'] = 6
print(myInfo)


# Modifying values for a key
    # dictionary['key'] = value
myInfo['age'] = '19'
print(myInfo)

# Removing Key value pairs
    # del dictionary['key']
del myInfo['Height']
print(myInfo)

# Looping through A dictionary
for key , value in myInfo.items():
    print("key : " + key + " Value : " + value)

# Sorted Dictionaries
    # sorted(dictionary.values()) or sort(dictionary.keys())
print(sorted(myInfo.keys()))
print(sorted(myInfo.values()))

# dictionary inside a dictionary
user = {
    'name' : {
        'fName' : 'Hemang',
        'mName' : 'Hitesh',
        'lName' : 'Bhogayata'
    },
    'age' : 18,
    'email' : 'hemang@example.com'
}

print(user)