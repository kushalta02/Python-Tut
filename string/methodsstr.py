user_inp = input("Enter the text until enter is pressed : ")
print("Total no. of character entered are :",len(user_inp))
split_word=user_inp.split()
word_count=len(split_word)
print("Total no. of words entered are : ",word_count)
alpha_count=digit_count=spec_count=0
for alp in user_inp:
    if (alp.isalpha()==True):
        alpha_count+=1
    elif(alp.isdigit()==True):
        digit_count+=1
    else:
        spec_count+=1
print("Total no. of alphabets",alpha_count)
print("Total no. of digits are ", digit_count)
print("Total no. of special cases are : ",spec_count)

