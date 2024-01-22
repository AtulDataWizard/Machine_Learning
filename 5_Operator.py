#operators are used to perform operations
#Arithmatic operator (+,-,*,/,**,//)
print(20+3) #for addition
print(20-3) #for substraction
print(20*3) #for multiplication
print(20/3) #for division
print(20**3) #for power (20power3)
print(20//3) #for division that ignores the floating point and gives only integer
print(20%3) #gives the remainder

##logical operator (and, or , not)
#1and operator returns the next value is the first operand is true (non zero=true operand, zero=false operand)
print(10 and 0)   #output 0
print(0 and 0)    #output 0
print(1 and 10)   #output 10
print(10 and -1)  #output -1
print(-1 and 10)  #output 1

#2 or operator returns the first value if it is true else returns the next value
print("or operator")
print(10 or 0)   #output 10
print(0 or 0)    #output 0
print(1 or 10)   #output 10
print(10 or -1)  #output 10
print(-1 or 10)  #output -1

#3 not operator (gives boolean result if value is true it makes it as false and if the value is false it changes it to true)
print(not 0) #output true
print(not -1) #output false
print(not 12) #output false

##relational operator (>,<,<=,>=,==,!=) (returns boolean value)
a=10
b=20
c=10
print("relational operator")
print(a>b) #output false
print(a<b) #output true
print(a>=b) #output false
print(a<=b) #output true
print(a==b) #output false
print(a!=b) #output true
print(a==c) #output true

#membership operator(in, not in)
#the membership operators (in and not in) are used to test whether a value exists in a sequence
print("membership operator")
x="pedofile"
y="ped"
z="pdf"
print(x in y) #false
print(y in x) #true
print(z in x) #false

a=[10,20]
b=30
print(b not in a) #true

##relationship operator (is, is not)
#relationship operator The 'is' operator in Python is used to test whether two variables refer to the same object(address) in memory.
print("relationship operator")
a=[1,"Atul",89]
a=b
c=[1,"Atul",89]
print(a is b)    #True
print(a is c)    #False a is c: This is False because a and c are different objects in memory. Even though their contents may be the same, they are distinct lists
print(b is c)    #False

#bitwsie operator
a=2
b=1
print(a&b) #bitlevel operation
print(a|b)