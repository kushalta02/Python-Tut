def swap_case(s):
    strg=" "
    for i in s:
        if i.isupper()==True:
            # up=True
            strg+=i.lower()
            # strg+=i
            # print(strg)

        if i.islower()==True:
            # low=True
            strg+=i.upper()
            # strg+=i
            # print(strg)
        
    return strg
            

    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)