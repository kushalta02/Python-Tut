string=input("Enter a string :")
str=string[::-1]
print(str)
if string == str:
    print("It is a palindrome")
else :
    print("It is not a palindrome")
    if string.isupper():
        print(string.lower())
    elif string.islower():
        print(string.upper())