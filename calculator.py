# Python-Code
import math
while True:
  operation=input("Which operation do you want to do ?\n\n Type + for addition\n Type - for subtraction\n Type * for multipication\n Type / for divition\n Type % for Module\n Type ** for Power\n Type R for ROOT\n Type Log for logarithm\n Type Sin for sin\n Type Cos for cos\n Type Tan for Tan\n Type Gcd for gcd\n Type ! for factorial \n")
  def multiply(num_list):
      z = 1
      for num in num_list:
        z *= num
      print(z)
  def add(num_list):
    z = 0
    for num in num_list:
      z += num
    print(z)
  def power(a,b):
    z=math.pow(a,b)
    print(z)
  def sub(a,b):
    z=a-b
    print(z)
  def div(a,b):
    z=a/b
    print(z)
  def module(a,b):
    z=a%b
    print(z)
  def root(a):
    print(math.sqrt(a))
  def log(a):
    z=math.log10(a)
    print(z)
  def cos(a):
    z=math.cos(a)
    print(z)
  def sin(a):
    z=math.sin(a)
    print(z)
  def tan(a):
    z=math.tan(a)
    print(z)
  def gcd(a,b):
    z=math.gcd(a,b)
    print(z)
  def Factorial(a):
    z=math.factorial(a)
    print(z)
  def degree(a):
    z=math.degrees(a)
    print(z)
  if operation== "*":
    num_list=[]
    multiplyer=int(input("how many numbers you want to multiply"))
    for i in range(multiplyer):
      user_input=float(input("enter numbers::"))
      num_list.append(user_input)
      #print(num_list)
    multiply(num_list)
  elif operation== "+":
    num_list=[]
    adder=int(input("how many numbers you want to add"))
    for i in range(adder):
      user_input=float(input("enter numbers::"))
      num_list.append(user_input)
    add(num_list)
  elif operation== "-":
    a,b=float(input("num1::")),float(input("num2::"))
    sub(a,b)
  elif operation== "/":
    a,b=float(input("num1::")),float(input("num2::"))
    div(a,b)
  elif operation== "%":
    a,b=float(input("num1::")),float(input("num2::"))
    module(a,b)
  elif operation== "**":
    a,b=float(input("num1::")),float(input("num2::"))
    power(a,b)
  elif operation== "R":
    a=float(input("Enter number"))
    root(a)
  elif operation== "Log":
    a=float(input("Enter number::"))
    log(a)
  elif operation== "sin":
    a=float(input("Enter number::"))
    sin(a)
  elif operation== "Cos":
    a=float(input("Enter number::"))
    cos(a)
  elif operation== "Tan":
    a=float(input("Enter number::"))
    tan(a)
  elif operation== "!":
    a=float(input("Enter number::"))
    Factorial(a)
  elif operation== "Gcd":
    a,b=float(input("num1::")),float(input("num2::"))
    gcd(a,b)
  elif operation== "!":
    a=int(input("Enter number::"))
    degree(a)






