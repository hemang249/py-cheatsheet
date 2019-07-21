# Some Common String Functions Used In Python 3

# String Declaration
singleString = 'This Is A String with Single Quotes'
doubleString = "This Is A String with Double Quotes"
multiString = """This is a 
MultiLine String"""

print(singleString)
print(doubleString)
print(longString)

# STRING CONCATENATION
fName = "Hemang"
lName = "Bhogayata"
name = fName + " " + lName
print(name)

# WHITESPACE REMOVAL
    # strip()

whiteSpaceString = "There are 5 Spaces    "
print(whiteSpaceString.strip())

# STRING CASE CONVERSION
    # upper() , lower() , swapcase()

str1 = "THIS IS UPPERCASE"
str2 = "this is lowercase"
str3 = "CaSe SwAp"
print(str1.lower())
print(str2.upper())
print(str3.swapcase())


# String Searching 
    # find(string)

str3 = "The Quick Brown Fox Jumps Over A Lazy Dog"
str4 = "This is a string"
str5 = "This is not a string"
pos = str3.find("Lazy")
print(pos)


# Character Count
    # count(string)

str4 = "This Is a very very long string"
count = str4.count('a')
print(count)

# String Replacing
    # replace()

str5 = "Yet Another String"
print(str5.replace("Yet" , "Not"))
