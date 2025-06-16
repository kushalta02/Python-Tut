import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='khushipushi',
    database='Griv_sys'
)
mc=mydb.cursor()
user_id=input( " enter")
password=input(" ENTER ")
r=''
def d_box():
    
    
'''
def user_data():
    print(" ENTER REQUIRED INFORMATION --")
    global User_id
    User_id = input(" ENTER YOUR USER ID : ")
    user_nme = input(" NAME :")
    age=int(input(" AGE :"))
    contact_no=int(input(" CONTACT NO. "))
    address=input(" ADDRESS :")
    Email_id=input(" ENTER EMAIL ADDRESS :")

user_data()
print(User_id)
opt=["1.HEALTH AND SANITATION","2.SOCIAL PROBLEMS","3.ENVIRONMENT PROBLEMS","4.INFRASTRUCTURE SERVICES","5.DOCUMENT/RECORD MAINTENANCE PROBLEMS"]
for i in range(0,5):
    print(opt[i])
def runProgramToRepeat():
    keepRepeating = 1
    while keepRepeating:
        keepRepeating = programToRepeat()
def programToRepeat():
    again = input("Do you want to Submit another complaint(ANSWER IN FORM OF YES OR NO):- ")
    if again == "yes" or again=="YES" :
        ask=input(" ARE YOU ALREADY SIGNED IN ?")
        if ask=="YES" or ask=="yes":
            print("REPEATED")
        else:
            print("sign in ")
    else:
        print("THANKYIU ")
runProgramToRepeat()
programToRepeat()'''