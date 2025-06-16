def char_count(user_str):
    final = ' '
    v=" Total no. of vowels are : "
    s= " Total no. of spaces  are : "
    c= " Total no. of consonents are : "

    v_count=0
    spa_count=0
    c_count=0
    upda_str = user_str.lower()
    vowel=['a','e','i','o','u']
    for i in upda_str:
        if i in vowel:
            v_count+=1
        elif i.isspace():
            spa+=1
        else:
            c_count+=1
    final = v+ str(v_count) + s + str(spa_count) +c +str(c_count)
    return final
user_str=input( " Enter a string ")
print(char_count(user_str))
