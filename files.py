# Python has functions for creating, reading, updating and deleting files

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name ', myFile.name)
print('is closed ', myFile.closed)
print('mode ', myFile.mode)

# Write to file
myFile.write('i love python')
myFile.write(' and Go')
myFile.close()

#Append to file
myFile = open('myfile.txt', 'a')
myFile.write(', i also like javaScript')

# Read from file
myFile = open('myfile.txt', 'r+')
text =myFile.read(100)
print(text)
