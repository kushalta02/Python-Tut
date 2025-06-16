num1=int(input("Enter first number"))
num2=int(input("Enter second"))
a=num1
b=num2
while b!=0:
    num=b
    b=a%b
    a=num
gcd=a
lcm=int((num1*num2)/gcd)
print("LCM",lcm)
print("GCD",gcd)
