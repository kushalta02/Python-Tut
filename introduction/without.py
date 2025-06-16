#Python program to swap values of two variables without using the third variable
var1=input("Enter a number")#ask the input from the user
var2=input("Enter another number")
'''Swaping values without using the third variable and 
Using Comma operator instead to swap values'''
var1,var2 = var2,var1
print("The value of var1 and var2 after swaping is",var1,var2)
