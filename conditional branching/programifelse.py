#python program to count the no. of vowels and consonants in a string 


var= input("Enter any string : ")
vowel=['a', 'e', 'i','o', 'u','A','E','I','O','U']

vowel_count=0
consonant_count=0

for letter in var:

    if letter in vowel:
        vowel_count = vowel_count+1
    else:
        consonant_count = consonant_count+1
        
print(" No. of Vowel are : ", vowel_count, "\nNo. of Consonent are : ", consonant_count)
