s1="Abc"
s2="Xyz"
s1_len=len(s1)
s2_len=len(s2)
str3=s1[0]+s2[(s2_len)-1]+s1[(s1_len)-2]+s2[(s2_len)-2]+s1[(s1_len)-1]+s2[0]
print(str3)