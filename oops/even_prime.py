"""
    PROGRAM TO CHECK A NUMBER IS EVEN OR NOT AND ALSO TO CHECK THAT IT IS PRIME 
"""
#creating class
class Even_check:
    #creating function using __init__ class constructor 
    def __init__(self,raw_no):
        #specifying variables
        self.raw_no =raw_no
        self.ev=False
        self.res=""
        
    def even(self):
        #using exception handling 
        #testing a block of code
        try:
            #condition for even number
            if self.raw_no%2==0:
                #setting  the result if  condition is true
                self.ev=True
            
        #handles  occured exceptions
        except:
            self.ev=False
        #using if else to display result
        if self.ev:
            #overwriting 
            self.res=("THE NUMBER IS EVEN ")
        else:
            self.res=("THE NUMBER IS ODD")
        #returning final result
        return self.res
#creating another subclass by passing superclass as parmeter of subclass
#Using inheritance property to inherit methods and attributes of Even_check clas

class Numb(Even_check):
    def __init__(self,raw_no):
        #using class constructor 
        super().__init__(self)
        #specifying variables
        self.raw_no =raw_no
        self.pri=False
        self.output=""
    def prime(self):
        super().even()
        
        #using exception handling  same as above
        try:
            for i in range(2,self.raw_no):
            #checking the number is prime or not
                if self.raw_no %i ==0:
                    self.pri=True
                    break
        except:
            self.pri=True
        if self.pri:
            self.output=(self.raw_no," IS NOT   PRIME")
        else:
            self.output=(self.raw_no,"IS PRIME")
        return self.output
#creting an object i.e instance of our class

check=Numb(345)
#subclass containing attributes of super class
print(check.even())#attribute of Even_check class inherited by Numb class
print(check.prime())