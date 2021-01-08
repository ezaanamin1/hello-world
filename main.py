import math
def add(a,b):
    c=a+b
    return c
def multiplay(d,e):
    r=d*e
    return r
def divde(a,b):
    c=a//b
    return c
def mod(a,b):
    c=a%b
    return c
def square(a):
    c=a*a
    return c
def underroot(a):
   c=math.sqrt(a)
   return c


print("Calculator")
number=int(input("Enter first number"))
number2=int(input("Enter second number"))
print("Pick any options")
print("1.Add two number")
print("2.Multiplay two numbers")
print("3.Divide two numbers")
print("4.mod of two numbers")
print("5.square of a  numbers")
print("6.under-root of two numbers")
option=int(input("Choose any options"))
if option==1:
    print("Result is:")
    print(add(number,number2))
elif option==2:
          print("Result is:")
          print(multiplay(number,number2))
elif option==3:
    print("Result is")
    print(divde(number,number2))
elif option==4:
    print("Result is")
    print(mod(number,number2))
elif option==5:
    print("Result is")
    print(square(number))
    print(square(number2))
elif option==6:
    print("Result is")
    print(underroot(number))
    print(underroot(number2))









