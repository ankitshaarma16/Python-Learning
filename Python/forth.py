"""
Forth Class Note 
(4:06:19 to 4:30:35)
            
"""
#---------------------------Functions------------------------
#----
def greet():       # creates a function
    print("Hello, Namaste")

greet()    # calling the function

#-----Return-----------
def new():
    return "How are you?"  # return the value to new()
print(new())  # prints "How are you?"

#-----Parameters and arguments-----------

def sum(a,b):        # a and b are the parameters
    print(f"The sum of the numbers is {a + b}")

sum(2,4)  # 2 is assigned to a  and 4 is assigned to b are arguments (it prints 6)


#--------------Types of Arguments---------------

#-----Positional Argument-------
def sum(a,b):        # a and b are the parameters
    print(f"The sum of the numbers is {a + b}")

sum(2,4)  # 2 is assigned to a  and 4 is assigned to b are arguments (it prints 6)


#-------Keyword argument------
def intro(name,age):
    print(f"Hello, My name is {name} and age is {age}")

intro(age = 16, name="Ankit") # it prints (Hello,My name is Ankit and age is 16)

#------Default argument------

def sub(a,b=10):
    print(f"The difference is {a-b}")
sub(12)   # it prints (The difference is 2)