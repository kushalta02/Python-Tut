marks = [[92,53,56,40],
        [90,23,56,78],
        [98,88,45,65],
        [90,45,67,45,12]]
grades = []        
count1=0
while count1<len(marks):
    count2=0
    while count2< 4 :
        if marks[count1][count2]>90:
            grades.append('A')
        elif marks[count1][count2]>=76 and marks[count1][count2]<90:
            grades.append('B')
        elif marks[count1][count2]>61 and marks[count1][count2]<=75:
            grades.append('C')
        elif marks[count1][count2]>41 and marks[count1][count2]<=60:
            grades.append('D')
        elif marks[count1][count2]>25 and marks[count1][count2]<=40:
            grades.append('E')
        elif  marks[count1][count2]<25 :
            grades.append('E')
        
        
        count2+=1
    count1+=1
print(grades)


