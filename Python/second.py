"""
Second Class Note 
(59:10 to 2:16:12 )            
"""
#---------------------------------Operators--------------------------------------------

#-------------Arthimetic Operators--------------
a = 20
b = 10 
print(a+b) # prints 30
print(a-b) # prints 20
print(a/b) # prints 2.0
print(a//b) # print 2, the "//" is called floor division(removes the number after decimal)
print(5**2) # prints 25 , the "**" used to calculate the power
print(15%2) # print 1, the " % (MOD)" is used to calculate the remainder

#-------------Assignment operator------------------------
c = 20 # assign the value

#---------------Compound Assignment operator-------------
"""d = 30
d = d + 30 #value reassign
d = d + 40 #value reassign
print(d) #prints 100
"""
#-----or-------
d = 30
d += 30 #value reassign
d += 40 #value reassign
print(d) # prints 100

""" ----------Similarly in -,*,**,/ ------------------"""

#-----------------------Comparison Operators------------------------
e = 10
f = 10
print(e == f) #it prints True "==" is used to compare either it's equal or not 
print(e != f) # it prints False "!=" not equal
print(12 > 10) #it prints true
print(12 < 10) #it prints False
print(12 >= 10) # it prints True , ">=" (greater than or equal to)
print(12<=10) # it prints False , "<=" (smaller than or equal to)

# ---String Comparison -------
print(ord("A")) # it prints an unicode of A, which is 65(ASCII value)
print(ord("B")) # it prints an unicode of B, which is 66 (ASCII value)
print("A" > "B") # it prints False 
print("Ankit" > "Sharma") #it prints false

#----------------------------Logical Operators-------------------------------

print(12==10 and 12==12 and 12>10 )# prints false, when all condition are true
print(12==12 or 12>35 or 12<5) #prints true , when aleast one condition is true
print(not 12==12) # prints false , complement of the condition 


#--------------------------Conditional Statements(if else)-------------------------------------------------

#---------if-else-----------

a = 18
if a >= 18:
    print("You are applicable to vote!!")
else:
    print("You arenot applicable to vote!!")


#--------if-elif-else--------

age = int(input("Enter your age: "))
if age <= 3:
    print("You are baby...")
elif age < 18:
    print("You are minor...")
elif age <= 59:
    print("You are adult...")
else:
    print("You are elder...")
