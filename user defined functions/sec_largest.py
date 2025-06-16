def to_print_second_largest_element_of_list(raw_input):

    """
    Function to find the second largest element in a list of numbers 
    """
    sorted_list = raw_input.sort()
    return raw_input[len(raw_input)-2] # Subtracting 2 to obtain second last index as the list is sorted in ascending order So, it will be the largest second index
      
   

 
print(" The Second largest element of list is :-> ",to_print_second_largest_element_of_list(raw_input=[129,34,5]))# user will input list here 
