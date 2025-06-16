list1=[25,24,35,20,32,41]
list2=[]

for i in list1:
    if  i %2 !=0:
        str1=i*2
        list2.append(str1)


total=sum(list2)
print("Twice the sum of odd no. :",total)
