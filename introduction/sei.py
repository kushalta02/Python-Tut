x=int(input("Enter value of x "))
n = int(input("Enter value of n : "))
s=0
for a in range( n +1):
    s+=x**a
print("sum of series",s)