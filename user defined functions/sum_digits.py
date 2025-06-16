#Creating a funtion to compute sum of digits in a string
def to_calculate_sum_of_digits(raw_str):
    """
    Funtion to enter a string with digits and compute the sum of digits
    """

    digit_count = 0
    for check_digi in raw_str:
        if (check_digi.isdigit()==True):
            #if the string contains any digit it will be stored in digit_count and the sum of digits  will be computed 
            # only if it is integer 
            digit_count += int(check_digi)
            #Converting into integer and adding the values in digit_count 
            
    return digit_count #Returning the sum of digits in a integer 
#end of function

raw_str=input(" Enter a string : ")
cal_digit = to_calculate_sum_of_digits(raw_str) #calling of  function 
print(" The sum of digits entered in string  is :->",cal_digit ) #displaying output


 