#Program to find volume of sphere and hemisphere using math module
#importing the math module
import math
pi = 22/7
#giving the pi variable the mathematical value of pi
print("Enter 1 for volume of sphere and 2 for volume of hemisphere")
#asking the user choice, wheather they wanted to find the volume of sphere or hemisphere
choose=int(input("Enter 1 or 2"))
if choose==1:
#using if , elif to find volumes of two diff.shapes
    radius=int(input("Enter the radius of sphere"))#indententing the statements 
    volumesphere = (4/3)*math.pi*pow(radius,3)
    print( "Volume of Sphere is",volumesphere)#displaying the output
elif choose==2:
    r=int(input("Enter the radius of hemisphere"))#indententing the statements
    volumehemisphere = (2/3)*math.pi*pow(r,3)
    print("Volume of hemisphere is ", volumehemisphere)#displaying the output 
    
