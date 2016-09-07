# cook your code here
# cook your dish here
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))
num3 = int(input('enter the third number:'))
if (num1>num2) and (num1>num3):
    large = num1
elif (num2>num1) and (num2>num3):
    large = num2
else:
    large = num3
print("greater is",large)
