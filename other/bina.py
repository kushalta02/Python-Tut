import pickle
f=open("s.dat","wb")
l=[]
def data(r,n,m):
    l.append(r)
    l.append(n)
    l.append(m)
    stu.append(l)
stu=[[1,'ash',80],[2,'bhup',67],[3,'ken',70]]
a=int(input(" 1 for add 2 for change"))
if a==1:
    r=int(input("enter roll no "))
    n=input("enter name ")
    m=int(input("enter narks "))
    data(r,n,m)
else:
    ls=[]
    v=input("enter name")
    for i in range(0,len(stu)):
        if stu[i][1]==v:
       
            
        #print current data
            r=int(input("enter new roll no "))
            n=input("enter name ")
            m=int(input("enter marks "))
            ls.append(r)
            ls.append(n)
            ls.append(m)
            a=len(ls)
            stu[i]=ls
pickle.dump(stu,f)
f.close()
fo=open("s.dat","rb")
a=pickle.load(fo)
print(a)
fo.close()