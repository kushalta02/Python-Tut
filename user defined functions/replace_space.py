#Begining of funtion
def replace_space_with_hyphen(raw_sentence):
    """
    Function to replace whitespaces  with  hyphen in a sentence and return modified sentence 

    """
    combined_sentence = ' ' #taking an empty string 
    
    for space in range(len(raw_sentence)):
        if (raw_sentence[space]==' '): # len function also counts whitespaces indexes So, applying condition to insert hyphen in place of whiespace 
                                        # hyphen will we inserted in place of whiteplace 
            
            combined_sentence+='-'
        else:
            combined_sentence+=raw_sentence[space] #values at indexes withput space will be stored here 
    return combined_sentence #the funtion will return a combined sentence formed by applying if and else conditions
#end of funtion


raw_sentence = input(" ENTER A SENTENCE : ->") #taking input from user
modified_sentence = replace_space_with_hyphen(raw_sentence)#calling the created function
print(" The Modified Sentence with Hyphen is : -> ",modified_sentence) #displaying the specific output



    





