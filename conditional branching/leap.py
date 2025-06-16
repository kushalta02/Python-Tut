#to check the year is leap year or not
year=int(input("Enter the year","yyyy"))
if(yearlen==4):
    if(year%4):
        print("it is a leap year")
    else:
        print("it is not a leap year")
else:
    print("INVALID INPUT")
