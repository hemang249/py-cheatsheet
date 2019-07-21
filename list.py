# Lists and Common List Operations In Python

#List Declaration
fruits = ['Apple', 'Orange', 'Strawberry', 'Mango']
print(fruits)

# Access Individual List Element
    # list[index]
print(fruits[0])
print(fruits[-2])

# Add Elements to the List
    # append(value)
fruits.append('Pineapple')
print(fruits)

# Insert Element at a particular index
    # insert(index , value)
fruits.insert(0 , 'Banana')
print(fruits)

# Delete Element at a particular index
    # del list[index]
del fruits[0]
print(fruits)

# Pop Elements from List
    # pop(index)
fruits.pop(0)
print(fruits)

# Remove all occurences of an Value
    # remove(value)
fruits.remove('Mango')
print(fruits)

# Sorting a List
    # sort()
numbers = [7,6,51,64,123,84]
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)

# Find List Length
    #len(list)
print(len(numbers))

# Looping through Lists
for fruit in fruits:
    print(fruit)

# Creating Ranged Lists
    # list(range(start , end , step))
rangedList = list(range(1,5))
print(rangedList)

# Max and Min in a list
    # max(list) , min(list)
print(max(numbers))
print(min(numbers))

# List Slicing
    # list[startIndex : endIndex+1]
print(numbers[0 : 3])



