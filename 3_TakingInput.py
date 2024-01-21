a=input("Enter your name ") #by default input statement takes string as input
print(a) #output Atul
a=input("Enter the first number ")
b=input("Enter the second nummber ")
print(a+b)
#output
'''let a=10
       b=20
       output=1020 [as a and b are strings so the a+b is just concatination of string]'''
#input command gives us string irrespective of what the user has given as input

#Typecasting
a=int(input("Enter the first number "))
b=float(input("Enter the second number "))
print(type(a))   #output int
print(type(b))   #outout float

a='2.7'
b=float(a)   #string to integer
print(b)

a=24
b=repr(a)   #integer to string
print(b," ", type(b))

#Fah to celcius calculator
#c=(f-32)*5/9
f=float(input("Enter the fahernheit temprature "))
c=(f-32)*5/9
print(c) #in float
ci=int((f-32)*5/9)
print(ci)
