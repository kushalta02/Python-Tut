def convert_string_to_title_case(raw_str):
#string is passed as a parameter as a variable
    """
    Function to convert a string to title i.e each word of the string will we capitalized
    
    """
    return raw_str.title()
raw_str = input(" Enter String to convert it into title case :- ")
title_str = convert_string_to_title_case(raw_str)#calling the created function 
print("Converted Title case string is :-> ",title_str)
