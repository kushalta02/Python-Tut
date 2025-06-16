def to_print_largest_element_of_list(raw_list): # Taking list as a parameter 
    """
    Function to print the largest element i.e largest number  of  a list  
    
    """
    ascend_list = raw_list.sort() #this will sort the list in ascending order and thus the element at the last index will be the largest
    return raw_list[len(raw_list)-1] # subtracting 1 to obtain the last index
    # end of funtion 

final_list = to_print_largest_element_of_list(raw_list=[23,46,899,999]) #enter the list of numbers here
print(" The largest number in the list is : ",final_list)
                                                                            
