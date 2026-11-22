"""
Third Class Note 
(2:16:12 to )            
"""
#----------------------------Loops------------------------------------

#--------For-Loop----------------
#1----
for i in range(1,10,1):      #range(start,stop,steps or differences)
    print(i) #it prints 1,2,3,4,5,6,7,8,9

#2-----
a = range(5) #default starting point "0" and default steps "1"
for i in a:
    print(i) #prints 0,1,2,3,4

#---Reverse Loop-----
#1-----
for i in range(5,0,-1):
    print(i) #prints 5,4,3,2,1

#2----
for i in range(-5,-10,-1):
    print(i) #prints -5,-6,-7,-8,-9
    

#3-----(Printing a table of 5)
for i in range(5,51,5):
    print(i)

#---------for-loop in Strings--------------
#1-------
b ="Ankit"
for i in range(5):       #range(0,5,1)
    print(b[i]) #prints A,n,k,i,t  print(b of i)

#2---------
c = "Ankit is a programmer"
print(len(c)) #prints length of "c" (starting point of counting is 1)
for i in range(len(c)):
    print(c[i]) #prints Ankit is a programmer

#3 (reverse of string)--------
n = "Ankit"
a = ""
for i in range(len(n)-1,-1,-1):
    a = a + n[i]
print(a)



#--------------Break of loop-------------------

for i in range(5):    #------------,
    if i == 2:                    #|_____ it prints (0,1)
        break                     #|                      #|
    print(i)          #------------'



#--------------Continue in loop--------------
for i in range(5):    #------------,
    if i == 2:                    #|_____ it prints (0,1,3,4)
        continue    #miss 2       #|
    print(i)          #------------'      
                     

