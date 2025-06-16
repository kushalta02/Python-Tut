#from to_find_prime_with_function import check_prime

inp_num=int(input("Enter a no."))
if inp_num==1:
    print("It is neither composite nor prime")
is_prime=True
if inp_num > 1:
    for d_num in range(2,inp_num):
        if inp_num%d_num==0:
            is_prime=False
    print(inp_num,is_prime)


    