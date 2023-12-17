people = ['Tobby', 'Wis', 'Ruon']

# Simple loop
for person in people:
    print(f'current person: {person}')

# Break
for person in people:
    if person == 'Wis':
        break
    print(f'current person: {person}')

# Continue
for person in people:
    if person == 'Wis':
        continue
    print(f'current person: {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0 ,11):
    print(f'number: {i}')

# While loops
count = 0
while count <= 10:
    print(f'count: {count}')
    count += 1