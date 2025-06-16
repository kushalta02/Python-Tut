str = input("Enter a string :  ")
num = int(input("Enter the nth index you want to remove : "))
modified_str =' '


if num <len(str):
    for i in range(0,len(str)):
        if i!=num:
            modified_str += str[i]
    print("The string after removal of nth term is",modified_str)
else:
    print("GIVEN INDEX IS NOT AVIABLE")
    