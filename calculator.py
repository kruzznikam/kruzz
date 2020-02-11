def add(x , y):
  return x+y

def sub(x , y):
  return x-y

def mul(x , y):
  return x*y

def div(x , y):
  return x/y

print("Select option , 1 2 3 4")

choice = input("Enter option")

num1 = float(input("Enter Number 1"))
num2 = float(input("Enter Number 2'))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", sub(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", mul(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", div(num1,num2))
else:
   print("Invalid input")
