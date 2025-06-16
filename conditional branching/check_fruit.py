# Program to check fruit entered by user is available at the shop or not 
fruits=["Apple","Mango","Banana","Grapes","Cherry","Strawberry"]
user_item = input("Enter the fruit needed :")
if user_item in fruits:
    print("The particular fruit is available at our shop")
elif user_item not in fruits:
    print(" We are Sorry , The fruit is not availavle ")

