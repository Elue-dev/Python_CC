def sayHello(name):
    print(f'Hello {name}')

sayHello('Wisdom')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

result = getSum(3, 4)
print(result)

# Lamda function: small anonymous function, can take any number of arguments but can only have one expression. 
# Very similar to js arrow function

getSum = lambda num1, num2 : num1 + num2
print(getSum(10, 20))