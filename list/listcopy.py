'''
w = input("enter a word")
if w =='Hello':
    print("Ok")
else :
    print("not ok")
N=4
M=[25,8,75,12]
for i in range(N):
    if M[i]%5==0:
        M[i]//=5
    if M[i]%3==0:
        M[i]//=3
for i in M:
    print(i,end='#')'''
import random
colours=['violet','indigo','blue','green','yelloe','orange','red',]
end=random. randrange(2)+3
begin=random. randrange(end)+1
for i in range(begin,end):
    print(colours[i],end = "&")
        




    


    
    
