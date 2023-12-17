name = 'Wisdom'
age = 10


# Arguments by position
# print('My name is {name} and I am {age} years old'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'My name is {name} and I am {age} years old')

s = 'hello world'

#Capitalize string
print(s.capitalize())
print(s.casefold())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace('world', 'everyone'))
print(s.startswith('hello'))
# Count
sub = 'o'
print(s.count(sub))
#Split into list (array)
print(s.split())
print(s.find('r'))