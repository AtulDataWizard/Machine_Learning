a=int(input("Enter the first number"))
c=input("Enter the operator")
b=int(input("Enter the second number"))

match c:
  case "+":
    print(f"Addtion of {a} and {b} is {a+b}")
  case "-":
    print(f"Substraction of {a} and {b} is {a-b}")
  case "*":
    print(f"Multiplication of {a} and {b} is {a*b}")
  case "/":
    print(f"Division of {a} and {b} is {a/b}")
  case "%":
    print(f"Remainder of {a} and {b} is {a%b}")
  case "hello":                                             #case statements can take string and numeric value
    print(f"Power of {a} to {b} is {a**b}")
