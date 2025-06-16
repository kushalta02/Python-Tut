#Program to reverse a number and perform different calculations
frst_num=(input("Enter a number : "))
second_num=(input("Enter a another number : "))
rev_frst=frst_num[::-1]
rev_second=second_num[::-1]
sum = int(rev_frst) + int(rev_second)
print(" Sum of two numbers after reversing is : ",sum)
difference =int(rev_frst)-int(rev_second)
print(" Differnce of two numbers after reversing is : ",difference)
product = int(rev_frst)*int(rev_second)
print(" The product of two numbers after reversing is : " ,product)
division = int(rev_frst)/int(rev_second)
print("The division of two numbers after reversing is :",division)
modulus = int(rev_frst)%int(rev_second)
print(" The modulus of two numbers is :",modulus)
exponential = int(rev_frst)**int(rev_second) 
print(" The exponential of two numbers after reversing is :",exponential)
floor_div =  int(rev_frst)//int(rev_second) 
print(" The floor division of two numbers after reversing is :",floor_div)