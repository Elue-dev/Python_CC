# File containing a set of funnctions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core modules
import datetime
from datetime import date
import time
from time import time

# Pip modules
from camelcase import CamelCase

# Custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
# timestamp = time.time()
timestamp = time()

c = CamelCase()

email = 'test@test.com'
if validate_email(email):
    print('email is valid')
else:
    print('email is not valid')

# print(today)
# print(timestamp)
# print(c.hump('hello there world'))
