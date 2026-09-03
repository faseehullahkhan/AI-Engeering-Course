print("Hello, World!")
# Some basic data types in Python
a = -34
b = 12
c = a/b
print(type(c))

v = 12j
print(type(v))
print(v.real) 

b = True
print(b)

# ord and chr
F = 'A'
print(ord(F))

G = 20
# print(chr(G))

# So ORD can change the character to its ASCII value and chr can change ASCII to character

str = 'Faseeh'
print(str[3])
# or
print(str[-6], str[0])
name = "Faseehullah khan"
print(name[0 : 5 : 1]) # string slicing

# Type coversion

# weather = 'Raining'
# weather = int(weather)
# print(type(weather))

number = '21'
print(type(number))
number = int(number)
print(type(number))
# these are the expilict type conversion , here we use fucntions to do the conversion
# int() , float() ,str() , bool()

weather = ''
weather = bool(weather)
print(type(weather))
print(weather)

# now implicit - this conversion is done by python automatically
i = 12
print(i/4) # the result will be floating point value

name = 'Faseeh'
age = 23
print(f'my name is {name} and age is {age}')



# Questions
# Accept the number from the user and accept the age from the user
num = int(input("Please enter your number"))
user_age = int(input("Please enter your age : "))
print(f'User number is {num} and user age is {user_age}')