#Program to input number and display largest or smallest number 
raw_input = input("Enter a list of numbers(seprated by ',') : "  )#asking user a list of numbers
nums=raw_input.split(',')#Using split function to split the input individually 
choice=int(input("Enter 1 for largest and 2 for  smallest  " ))#Asking the user choice 
if choice==1:
    print("The Largest number among the given numbers is : ",max(nums))#Using max function to display
    #largest number''
elif choice==2:#Execution will only take place when if condition is not met
    print("The Smallest number amomg the given numbers is : ",min(nums))#Min function to find the smallest
   

