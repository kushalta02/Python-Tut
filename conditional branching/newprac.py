num1=int(input("Enter a number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))
if (num1>=num2)or(num1>=num3):
    largest = num1
elif (num2>=num1)or(num2>=num3):
    largest = num2
else:
    largest = num3
print("the largest no is ",largest)
