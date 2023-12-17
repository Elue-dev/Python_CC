import json

# Sample JSON
userJSON = '{"first_name": "Wisdom", "last_name": "Elue"}'

# Parse to dictionary
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# Turn dictionary to JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)

print(carJSON)
