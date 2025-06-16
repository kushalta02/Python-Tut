yer=input("Enter the year:(yyyy)")#taking input from the user in the form yyyy
if len(yer)==4:#Conditional branching
#set of statements will only execute if the condition is met
    if int(yer)%4==0:#taking integer input to perform mathematical operations
        print("it is a leap year")
    else:
        print("it is not a leap year")
else:
    print("Invalid input")#Control goes to else only when the if condition is not met
