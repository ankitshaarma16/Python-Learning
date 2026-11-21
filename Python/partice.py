#--------------1--------------------- 
"""
gender = str(input("Enter you gender(Male or Female):")).lower()
if gender == "Male":
    print("Good Afternoon sir")
elif gender == "Female":
    print("Good Afternoon mam")
else:
    print("Invalid Input")
"""
#-----------------2------------------
"""
num = int(input("Enter any number:"))
if num%2 ==0 :
    print("Even number")
else:
    print("Odd number") 
"""

#---------------------3----------------
"""
name = str(input("Enter your name:"))
age = int(input("Enter your age:"))
if age>=18:
    print(f"Hello {name}, you are a valid voter....")
else:
    print(f"Hello {name}, you are an invalid voter....")
"""

#---------------4-----------------------
"""
temp = int(input("Enter the surrounding temperature(`C):"))
if temp <= 0:
    print("Freezing cold")
elif temp <=10:
    print("Very Cold")
elif temp <=20:
    print("Cold")
elif temp <=30:
    print("Pleasant")
elif temp <=40:
    print("Hot")
elif temp >=40:
    print("Very Hot")
else:
    print("Invalid Temperature inputed.......")

#--------------5 table-------------------
n = int(input("Enter any number:"))
for i in range(n,n*11,n):
    print(i)

    
#---------6------------
n = int(input("How many times do you want to print:"))
for i in range(n):  
    print("Hello world")        

#----------7-------------
num = int(input("Any number"))
for i in range(1,num +1):
    print(i)
    
#----------8-----------
n = int(input("Any number:"))
for i in range(1,11):
    a = n * i
    print(f"{n} * {i} = {a}")

#----------9 (Find factroial value-----------
n = int(input("Any number:"))
f = 1
for i in range(1,n+1):
    f = f * i
print(f"The factorial value is {f}")


#------------10 (sum of even number and odd number in the given range)------
n = int(input("Any number:"))
a = 0
for i in range(2,n+1,2):
     a = a + i 
print(f"The sum of even number in your number range:{a}")
b = 0
for j in range(1,n+1,2):
     b = b + j
print(f"The sum of odd number in your number range:{b}")
"""