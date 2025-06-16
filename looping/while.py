marls_in=input("enter marks septated by coma")
marks=marls_in.split(",")
count=0
sum=0
while count<len(marks):
    sum+=int(marks[count])
    count+=1

