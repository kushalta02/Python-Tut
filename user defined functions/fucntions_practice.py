
# user def fun

# def 
# calling 

#------------------------------------------ Function without return value

# definition
def say_hello(name=None):
   #func body
    if name==None:
       print("Please provide name parameter")
    else:
       print("Hello, {name}".format(name=name))


#calling
# say_hello(name="khushi")

#------------------------------------------ Function with return value
def sq(num):
    if num==5:
        return num*num
    return 0

x=5
# print(sq(x))

#------------------------------------------ Function with return value

# 1.get str from user  -> i am a student
# 2. convert str to title case using .title() func 


def convert_str_to_title(raw_str):
    """
    Function to convert string to title case string i.e. each word of string is capitalize
    """
    return raw_str.title()

raw_str=input("Enter string to convert into titlecase :-> ")

titlecase_str = convert_str_to_title(raw_str)
print("Title case string is :-> ",titlecase_str)

# print(convert_str_to_title.__doc__)