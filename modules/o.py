import random
val=[80,70,60,50,40,30,20,10]
start=random.randint(1,3)
end=random.randint(start,4)
for I in range(start,end+1):
    print(val[I],"*")