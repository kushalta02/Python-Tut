#Program to swap values of two variables using the third variable
num1=input("Enter a number :")#ask the input from the user(firstvariable)
print(num1)
num2=input("Enter another number:")#ask another input and store it as variable(second variable)
print(num2)
#Using third variable for  swaping the values of the other two variables  
thirdvar=num1
num1=num2
num2=thirdvar
print("the values of num1 and num2 after swaping variables ",num1,num2)
