def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

print("Select operation : ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
  choice = input("Select operation you need to perform < 1,2,3,4 > : ")
  
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number :"))
      num2 = float(input("Enter second number :"))
    except ValueError:
      print("Oops! Invalid Input. Please Enter a number")
      continue
  
    if choice == '1':
        print("Ans is : ", add(num1, num2))
    
    elif choice == '2':
          print("Ans is : ", sub(num1, num2))

    elif choice == '3':
          print("Ans is : ", multiply(num1, num2))
    
    elif choice == '4':
          print("Ans is : ", divide(num1, num2))
    
  next_calculation = input("Would you like t0 continue < yes/no > : ")
  
  if next_calculation == "no":
    break
  else:
    print("Invalid Input")
    
  
      