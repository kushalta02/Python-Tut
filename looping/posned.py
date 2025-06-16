'''user_inp = int(input(" Enter a number :"))
if user_inp>=0 :
    print(user_inp," is a postive integer ")
else:
    print(user_inp," is a negative integer")
raw_str= input("Enter a sentence ")
vowel=consonent=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in raw_str:
    if i in vowels:
        vowel+=1
    else:
        consonent+=1
print(" Total no. of vowels ",vowel)
print(" Total no. of consonents ",consonent)'''
# Sqaure if even number 
x=1
while x<=10:
    if x%2==0:
        print(x*x)
    else :
        print("it is odd no")

    x+=1

