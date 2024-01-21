#Variable are the bucket where we store data
#Variable names are case sensitive
A=10
a=1

#Valid varibale name can only start with a-z/A-Z/_
abc=1 #valid
_="Atul" #valid
# 1abc=10 #not valid
# @a=2 #not valid
# %a=10 #not valid
i='a' #valid
ab_12=10 #valid

a=10
a+1
print(a) #The output will be 10 as I didnt assign the result back to the variable a so the value of a remains unchanged.

b=10
b+=1 #b=b+1
print(b) #output 11

a="Atul"
print(a*3)         #AtulAtulAtul
print("Anjali"*3)  #AnjaliAnjaliAnjali



#print('I have eaten ' + 99 + ' burritos.') #Throws error(can only concatenate str (not "int") to str)

x = True
y = False 
print(x)  #True

#to find the address of some variable we use id() func
a=10
b=a
c=11
print(id(a))  #output 1504   
print(id(b)) #output 1504
print(id(c)) #output 1505
#id of a and b are same as they are pointing to the same number
print(id(a) == id(b)) 
#output true
print(id(a) == id(c))  
#output false
