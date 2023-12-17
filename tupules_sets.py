# Tupule - collection which is ordered and unchangable. Allows duplicate members.

fruits = ('Apples', 'Mangoes', 'Oranges')

fruits2 = ('Apples',) #must end with trailing comma when only one item present or else it will see it as a string

# Delete tupule
del fruits2

# print (fruits2, type(fruits2))
# print(fruits2)
# print(len(fruits))

# Set - collection which is unordered and unindexed. No duplicate memebers.

# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Apples') # won't add cause its a duplicate
fruits_set.add('Grape')
fruits_set.remove('Mango')
# fruits_set.clear()

print(fruits_set)
