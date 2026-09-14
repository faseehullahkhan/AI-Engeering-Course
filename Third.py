# Conditional-Statements
# money = int(input("Please enter your amount"))
# if money > 20:
#     print("yes you can buy shitt")
# else:
#     print ("Earn more you dumb")

# num1 = int(input("Please enter number 1 : "))
# num2 = int(input("Please enter number 2 : "))

# if num1 > num2:
#     print(f" num-1 : {num1} is greater then num-2 : {num2}")
# elif num1 < num2:
#     print(f" num-2 : {num2} is greater then num-1 : {num1}")
# else:
#     print("Numbers are equal")

# leap year question - easy solution
# we have two types of leap years one are century years like 2000 , 3000 
# and the other are normal years like 1999, 2026...
# now to check, if the year is the century year it should be divided by 100 and as well as 400
# And the non-century years should be divided by 4

# year = int(input("please enter the year to check whether its a leap year or not : "))
# if year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year")
# elif year % 4 ==  0 and year % 100 != 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# name = "Faseehullah khan"
# print(name[0 : 5 : 1]) # 5 not included
# a= range(0 ,20 ,2)

# for i in a:
#     print(i, " ")


table = int(input("Please enter a number : "))
for i in range(1 , 11 , 1):
    print(f"{table} x {i} = {table * i}")