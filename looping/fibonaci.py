from typing import no_type_check


n_terms= int(input("Enter how many values ?"))
n1,n2= 0,1
count = 1
sum=0
print("Fibonacci Series",end = " ")
while count<=n_terms:
    print(sum,end = " ")
    count+=1
    n1=n2
    n2=sum
    sum=n1+n2
