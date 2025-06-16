raw_string=input("Enter a string : ")
vowel_count=0
consonant_count=0
uppercase_count=0
lowercase_count=0

vowel=['a','i','o','u','e','A','E','I','O','U']
for i in raw_string:
    if i in vowel:
        vowel_count+=1
    if i not in vowel:
        consonant_count+=1
    if (i.isupper()):
        uppercase_count = uppercase_count+1
    elif (i.islower()):
        lowercase_count = lowercase_count+1
print("No. of vowels",vowel_count)
print("No. of consonant ",consonant_count)
print("No. of uppercase character",uppercase_count)
print("No. of lowercase character",lowercase_count)