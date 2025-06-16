low_inp=int(input("Enter the number from which the sum should calculated  : "))
up_inp=int(input("Enter the end number upto which sum should be calculated  : "))
sum=0
for i in range(low_inp,up_inp):
    sum=sum+i
print("Sum of integers within given range", low_inp,"and",up_inp,"is",sum)
