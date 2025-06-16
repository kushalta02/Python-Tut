a=int(input("Enter first number:  "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
d=[]
d.append(a)
d.append(b)
d.append(c)
if a!=b!=c:
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if(i!=j&j!=k & k !=i):
                    print(d[i],d[j],d[k])
elif a==b==c:
    print("Only one combination is possible")