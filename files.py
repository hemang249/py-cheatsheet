# Working with Files In Python 3 

# Reading Data From A file
with open('file1') as file_object:
    data = file_object.read()
    print(data)

# Reading Data Line by line
with open('file2') as file_object:
    for line in file_object:
        print(line)

# Writing Data to a File
file_name = 'file3'
with open(file_name , 'w') as file_object:
    file_object.write("This is A Writing Test")

# Appending Data to a File
with open(file_name , 'a') as file_object:
    file_object.write("\nThis is Appending Test")