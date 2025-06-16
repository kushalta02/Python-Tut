str1="abcdefghijk"
num=len(str1)
print(num)
newval=(num//2)-1
print(newval)
str3=newval+2
while newval<=str3:
    print(str1[newval])
    newval+=1