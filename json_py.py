# Working With json Files in Python3
import json

# Storing Data in Form Of a Json File
numbers = [1,2,3,4,5,6]
file_name = 'Numbers.json'
with open(file_name , 'w') as file_object:
    json.dump(numbers , file_object)

# Loading Data From A Json File
with open(file_name) as file_object:
    num = json.load(file_object)

print(num)