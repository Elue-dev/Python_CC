# Collection which is unordered, changable and indeced. No duplicate members.

# Create dictionary
person = {
    'first_name': 'Wisdom',
    'last_name': 'Elue',
    'age': 26
}

# Use constructor
person2 = dict(first_name = 'Dubem', last_name = 'Elue')

# Get Value
print(person['first_name']) 
# OR
print(person.get('last_name')) # most common way

print(person2, type(person2))

# Add key/value
person['phone'] = '00000000000'
print(person)

# Get keys
print(person.keys())

# Get items
print(person.items())

# Copy dictionary
person2 = person.copy()
person2['city'] = 'Lagos'
print(person2)

# Remove item
del(person['age'])
# OR
person.pop('phone')
print(person)

# Clear
person.clear()
print(person)
print(len(person2))
print(person2)

# List of dictionaries
people = [
    {'name': 'martha', 'age': 30},
    {'name': 'kevin', 'age': 27},
    {'name': 'james', 'age': 22},
]

print(people)
print(people[1])
print(people[1]['name'])