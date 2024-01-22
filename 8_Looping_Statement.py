#Repeating certain lines for n amount of time
#for loops works on the concept of iterator and iterable
#iterable are object which can be broken down in smaller parts for example array,string,tuple,dic etc
#An iterator is an object that represents a stream of data

#sum of first n natural number
a=int(input("Enter the number you want to till sum of "))
sum=0
for i in range(1,a+1):
    sum+=i
print(f"Sum is {sum}")

#fibonacci
a=int(input("Enter the number "))
num1=0
num2=1
for i in range(a-1):
    if(a==0 or a==1):
        print(a)
        break
    c=num1+num2
    num2,num1=c,num2
    print(c)
    if(i==a-2):
        print(c)

#print all prime
a=int(input("Enter the range "))
for i in range(2,a+1):
    for j in range (2,i):
        if(i%j==0):
            break
    else:
        print(i)

'''Problem Description: You are given with a number N and a choice C. If the user enters C equal
to 1, then print sum of 1 to N numbers, but if user enters C equal to 2, then print product of 1 to
N numbers and if user enters any other value of C then print -1.'''

choice=int(input("Enter the choice "))
match choice:
    case 1:
        a=int(input("Enter the range "))
        total_sum=0
        for i in range(1,a+1):
            total_sum+=i
        print(f"Sum is {total_sum}")
    case 2:
        a=int(input("Enter the range for multiplication "))
        mul=1
        for i in range(2,a+1):
            mul=mul*i
        print(f"Multiplication till {a} is {mul}")
    case _:
        print("Invalid choice")

'''
Write a program to print first x terms of the series 3N + 2 which are not multiples of 4.
'''
x=int(input("Enter the number "))
for i in range(1,x+1):
    val=(3*i)+2
    if(val%4==0):
        x+=1
        continue
    else:
        print(val)
    

'''Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.'''
num=int(input("Enter the number "))
rev=0
while(num>0):
    if(num%10==0):
        num=int(num/10)
        continue
    last_dig=num%10
    rev=rev*10+last_dig
    num=int(num/10)
print(rev)

#Square Root
num=int(input("Enter the number you want to find root of "))
i=1
while(i<=num):
    if(i*i>=num):
        if(i*i==num):
            print(i)
            break
        else:
            print(i-1)
            break
    i+=1
