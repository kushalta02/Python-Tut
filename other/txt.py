b=open("k.txt","w")
k = ('i am yays','khus')
j=b.writelines(k)
b.close()
a=open("k.txt","r")
m=a.readline3()
for i in range(0,len(m)):
    print(m[i],"#")
a.close()