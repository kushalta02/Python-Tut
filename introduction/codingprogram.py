import math
print("Enter the coefficient in the form ax^2+bx+c")
list1=[]
frst_num=int(input("Enter the coefficient of x^2 : "))
second_num=int(input("Enter coefficient of x : "))
third_num= int(input("Enter  constant term : "))   
list1.append(frst_num)
list1.append(second_num)
list1.append(third_num)
print("The quadratic equation obtained is :\n",frst_num,"x^2","+",second_num,"x","+",third_num)  
d=second_num*second_num - 4 * frst_num* third_num
if d > 0:
    print("Roots are Real")
elif d == 0:
    print("Roots are real and equal")
else:
    print("Imaginary roots")
x=int(input("enter value of x :  "))
sum1=0
for i in range(len(list1)):
    sum1= sum1 + list1[i]*math.pow(x,len(list1)-(i+1))
print("The value of polynomial is",sum1)
