# 1. ADD
# 2. SUB
# 3. MUL
# 4. DIV

print("Selected an operation to perform:")
print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")

operation = input()
if operation == "1":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The Sum is: " + str(int(num1)+int(num2)))
elif operation == "2":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The Difference is: " + str(int(num1)-int(num2)))
elif operation == "3":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The Product is: " + str(int(num1)*int(num2)))
elif operation == "4":
     num1 = input("Enter first number: ")
     num2 = input("Enter second number: ")
     print("The Result is: " + str(int(num1)/int(num2)))   
else:
     print("Invalid Entry")


