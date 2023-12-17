x = 10
y = 12

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# if else
if x > y:
    print(f'{x} is greater than {y}')
else:
 print(f'{x} is less than {y}')


# else if
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
 print(f'{x} is equal than {y}')
else:
 print(f'{x} is less than {y}')

# Nested if
if x > 2:
    if x <= 9:
        print(f'{x} is greater than 2 and less than or equal to 9')
    else:
        print(f'{x} is greater than 2 and not less than or equal to 9')
else:
        print(f'{x} is less than 2')

if x > 2 and x <= 10:
    print(f'{x} is both greater than 2 and less than or equal to 10')

if x > 2 or x <= 10:
    print(f'{x} is both greater than 2 and less than or equal to 10')

if not(x == y):
    print(f'{x} is not equal to {y}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object 
numbers = [1,2,3,4,5]

# in
if x in numbers:
    print(x in numbers)

 # not in
if x not in numbers:
    print(x not in numbers)

# Identity operators (is, is not) - Compare the objects not if they are equal, but if they are actually the same object, with same memory location
    
# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)