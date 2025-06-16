str=input("enter ")
vowels=['a','e','i','o','u']
v_count=c_count=u_count=0
for i in str:
    if i in vowels:
        v_count+=1
    elif i not in vowels:
        c_count+=1
    elif(i.isupper()):
        u_count+=1
print(v_count,c_count,u_count)

        