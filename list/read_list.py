# Program to read a list of n integers and create different list of positive and negative integers
raw_int= int(input(" Enter how many elements you want to store in a list : ")) # asking for no. of integers
orig_list=[]    #taking empty list
positive_list=[]
negative_list=[]
for dig in range(raw_int):
    raw_list = int(input(" Enter elements of  list :->")) #Askind user for entering n number of elements
    orig_list.append(raw_list)
    if orig_list[dig]>=0: 
        positive_list.append(orig_list[dig]) # Will add positive integers to empty list 
    else:
         negative_list.append(orig_list[dig]) # Will add negative integers to empty list

print(" Total number of elements in the list are :- ",raw_int)                  
# Displaying all the lists as output
print(" The Original list of Positive and Negative integers is :-> ",orig_list)    
print(" The list of Positive integers is :-> ",positive_list)
print(" The list of Negative integers is :-> ",negative_list)