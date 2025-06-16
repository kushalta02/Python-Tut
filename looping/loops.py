marks=[[87,45,89,90,77,65,99,81],  #marks of class A
[56,45,90,91,39,69,76,50],
[56,78,89,77,59,78,30,89],
[78,95,36,21,82,95,84,69],
[98,76,51,43,67,91,84,33]]
'''count1=0
while count1<len(marks):
    count2=0
    while count2<8:
        marks[count1][count2]-=3
        count2+=1
    count1+=1'''
k=8 #5 classes 
for i in range(0,len(marks)):
    for j in range(0,k,2):
        if 
            k-=1
            
            marks[i][j],marks[i][j+1]=marks[i][j+1],marks[i][j]
print(marks) 
