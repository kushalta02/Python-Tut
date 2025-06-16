#Program to find reverse of a three digit no.
raw_num = int(input("Enter a three digit no."))#taking integer input from the user
remain_raw = raw_num//100# Using Floor division operator(quiotent after dividing)
quot = raw_num%100#Using Modulas( Remainder )
numb = quot//10
anumb = quot%10
rev_num = (anumb*100)+(numb*10)+(remain_raw)#Multiplication to change digit's place  
print("Reverse of the number is ",rev_num)
