# Program to display  " Nizzfizz" if number is multiple of 2 and 5   and for neither  a multiple of any number display "none" ,for multiple
#  of either one of them display "Fizz"
user_num = int(input("Enter a number : "))
if (user_num%2==0 )and(user_num%5==0):
    print("Nizzfizz")
elif (user_num%2==0)  or (user_num%5==0):
    print("Fizz")
else:
    print("None")




