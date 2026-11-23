"""
First Class Note 
(00:00 to 59:10)            
"""

#  this is comment
"""This is multiline
doc string , for multiline comments"""

print("hello world")

#-------------------------------------------Variable--------------------------------------------------------------
a = 1
b = 2
c = 3
d = "Ankit"

# -----------------------Naming conventions-------------------------------------------

AnkitSharma = "boy" # pascal case 
ankitSharma = "boy" # camel case
ankit_sharma = "boy" # snake case

# ------------------------------Data types-------------------------------------------- 

#-----Numbers-----

e = 40 # integer 
f = 12j # complex  
g = 40.66 # float 

# String  Data type

h = "Hello guys i'm 12"


# Boolean  Data type

i = True 

# '------------------------String--------------------------------------'

# Indexing 
# Default indexing [0,1,2,3] , start from 0
j = "Ankit" 
print(j[0]) # it prints "A" 
print(j[2]) # it prints "k"  (positive indexing)
print(j[-1]) # it prints "t" (negative indexing)

#   String slicing 

k = "Ankit Sharma"
print(k[0:5:1]) # it prints "Ankit" ,syntax : [start:stop:steps]
print(k[6:12:1]) # it prints "Sharma" __________
#or                                             |
print(k[6::1])  # it also print "Sharma"________|        


#----------------------Data type conversion------------------------------------------

# ------------------Explicit Conversion--------------------------------

# ----int to str-----
l = 12 # integer
l = str(l) # converting to string
print(type(l)) # string 

#----- str to bool----
m = "hello" #str
m = bool(m) #converting
print(type(m)) # data type bool converted
print(m) # prints either True or False

#------------------Implicit Conversion-----------------------
l = 12/3
print(l) # output is 4.0 ( converting  by python)


#-----------------------------Formatting String-------------------------------------

name = "Ankit"
age = "16"
print(f"Hi,I'm {name} and I'm {age}.") #  "f" is formatting string ..prints (Hi,I'm Ankit and I'm 16.) 


#---------------------------------------INPUT / OUTPUT-----------------------------------------------------
agge = int(input("What is your age?:")) # int() is used to convert it in the integer
full_name = str(input("What is your name?:")) # str convert the input data in string 
print(f"Your name is {full_name}")
print(f"Age:{agge}")