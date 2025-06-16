import random
fix_num=500
user_guess=int(input("Enter any number from 0 to 1000 :"))
guess=random.randint(0,1000)
print(guess)
if fix_num <user_guess :
    print("Guessed number is larger than fixed no. by ",user_guess-fix_num)
elif fix_num>user_guess:
    print("Guessed number is smaller than fixed no.by",fix_num-user_guess)