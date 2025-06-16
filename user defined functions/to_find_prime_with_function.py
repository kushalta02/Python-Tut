def check_prime(num):
    is_prime = True

    for d_num in range(2,num):
        
        if num%d_num==0:
            is_prime = False
            break
        
    if is_prime:
        print("{} is a prime number.".format(num))
    else:
        print("{} is a not prime number, because it divides with {}".format(num,d_num))

#inp_num = int(input("Enter number : "))
#check_prime(inp_num)
