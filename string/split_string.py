str="GMA CITY PUBLIC SCHOOL IS AT SINGRIWALA HSP"
t=str.split(" ")
l=[]
k=3 
for x in t:
    if len(x)>3:
        l.append(x)
print(l)