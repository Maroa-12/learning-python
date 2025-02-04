print("hello world")
print("MAROA")
print('o----')
print('||||')
print('*'*10)
price = 10
price=20
rating = 4.9
name = 'Maroa'
is_published = True
print(price)
name = ('John Smith')
age = 20
is_new = True
name=input('What is ypour name? ')
print('Hi' + name)
name = input('What is your name?')
favorite_color =input('What is your favourite color?')
print(name + 'likes' + favorite_color)
birth_year = input('Birth_year ')
age = 2019 - int (birth_year)
print(type(age))
print(age)
print(type(age))
weight_lbs = input('Weight(lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
course = ("Python for beginners")
print(course)
course = '''  
Hi John
Here is our first email to you
Thank you
The support team
'''
print(course)
course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:5])
name = 'Jennifer'
print(name[1:-1])
First = 'John'
Last = 'Smith'
message = First + ' [' + Last + ' ] is a coder'
msg = f'{First} [{Last}] is a coder '
print(message)
print(msg)
course = 'python for beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('p'))
print(course.find('beginners'))
print(course.replace('beginners', 'absolute beginners'))
print(course.replace('p', 'j'))
print('python' in course)
print(10/3)
print(10//3)
print(10**3)
x = 10
x -= 3
print(x)
x = 2.9
print(round(x))
print(abs(-2.9))
import math
print(math.ceil(2.9))
is_hot = False
if is_hot:
    print("its a hot day")
    print("drink a lot of water")
else:
     print("its a cold day")
     print("wear warm clothes")
is_hot = False
is_cold = False
if is_hot:
    print('its a hot day')
    print("drink plenty of water")
elif is_cold:
    print("its a cold day")
    print("wear warm clothes")
else:
    print("its a lovely day")
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: {down_payment}")
has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print("elligible for loan")
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("elligible for loan")
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("elligible for loan")
temperature = 30
if temperature > 30:
    print("its a hot day")
else:
    print("its not a cold day")
name = "maroa"
if len(name ) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")
weight = int(input("weight: "))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
   converted = weight * 0.45
   print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1



