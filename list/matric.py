mat1=[[1,2],
      [3,4]]
mat2=[[3,4],
      [5,6]]
#a11=mat1[0][0]*mat2[0][0]+mat1[0][1]*mat2[1][0]
#a12=mat1[0][0]*mat2[0][1]+mat1[0][1]*mat2[1][1] 
#a21=mat1[1][0]*mat2[0][0]+mat1[1][1]*mat2[1][0]
#a22=mat2[1][0]*mat2[0][1]+mat1[1][1]*mat2[1][1]
che=0
count=0
while count<1:
    ai=0
    
    count2=0
    while count2<1:
        ai+=mat1[count][count2]*mat2[count][count2]
        count2+=1
    che+=ai
    count+=1
print(che)

