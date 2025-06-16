def to_count_occurence_of_an_element(raw_list,elem_occur): #begining of funtion 
    """
    Funtion to find the  number of times an element occurs in a list

    """
    if elem_occur in raw_list :

        return raw_list.count(elem_occur)# using inbuilt method to find the occurence of an element 
                     # The funtion will return the number of times an element occurrs in a list
    else : 
        print(" The element is not present in the list")


raw_list = input(" ENTER A LIST OF ELEMENTS :") 
elem_occur= input(" Enter the element whose occurence you want to calculate -> ") #asking user the element whose occurence is to be found
total_occur = to_count_occurence_of_an_element(raw_list,elem_occur) #Calling the funtion 
print( " Number of times element ", elem_occur," occurs in the list is :- " ,total_occur)
                

