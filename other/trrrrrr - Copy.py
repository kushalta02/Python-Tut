import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='khushipushi',
    database='Griv_sys'
)
print(" =========================== WELCOME TO ONLINE GRIEVANCE SYSTEM ==========================")
mycur=mydb.cursor()
def createUserTable():
    mycur.execute("CREATE TABLE Applicants_info (User_id VARCHAR(200),Password VARCHAR(100), Name VARCHAR(255), Age INTEGER(20),Contact_no BIGINT(255),Address VARCHAR(255), Email_id VARCHAR(100));")
    for k in mycur:
        print(k)
#createUserTable()
'''def al_data():
    mycur.execute(f'ALTER TABLE Applicants_info MODIFY Contact_no BIGINT;')

    mycur.execute(f'INSERT INTO Applicants_info VALUES("D17H","Dan17ish","Danish",17,87654329,"Chandigarh","Da12@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("F40N","Far40an","Faran",40,876543219,"Chandigarh","fa12@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("A21H","At21ish","Atish",21,987654321,"Jalandhar Model Town H.no.-1711","At21@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("S24A","San24aya","Sanaya",24,942764321,"Opp. of ITI street no.-40 H.no.-652 ,Hsp","San@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("N23A","Nai23ra","Naira",23,839765432,"Kapurthala","Naira@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("A26N","Am26man","Amman",26,305643213,"Ropar","Amman26@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("A21A","Ae21ena","Aeena",21,673241569,"Pathankot","Ae21@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("Z31A","Zo31ya","Zoya",31,7382965401,"Ludhiana","Zoya@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("T20N","Ta20run","Tarun",20,6353210928,"Patiala","Tarun@gmail.com")')
al_data()'''
import maskpass
'''def user_data():
    print(" ENTER REQUIRED INFORMATION --")
    global User_id
    User_id = input(" ENTER YOUR USER ID : ")
    global password
    p = maskpass.askpass(mask=' ')
    password=pwd
    global user_nme
    user_nme = input(" NAME :")
    global age
    age=int(input(" AGE :"))
    global contact_no
    contact_no=int(input(" CONTACT NO. "))
    global address
    address=input(" ADDRESS :")
    global Email_id
    Email_id=input(" ENTER EMAIL ADDRESS :")'''
def options():
            opt=["1.HEALTH AND SANITATION","2.SOCIAL PROBLEMS","3.ENVIRONMENT PROBLEMS","4.INFRASTRUCTURE SERVICES","5.DOCUMENT/RECORD MAINTENANCE PROBLEMS"]
            for i in range(0,len(opt)):
                print(opt[i])
            var=input("SELECT ANY ONE FROM ABOVE MENTION BY WRITING ITS NUMBER : " )
            raw_str=' '
            if var=='1':
                raw_str=input("Report your problem HEALTH AND SANITATION related issue : ")
            elif var=='2':
                raw_str=input("Report your problem SOCIAL PROBLEMS related issue : ")
            elif var=='3':
                raw_str=input("Report your problem ENVIRONMENT related issue: ")
            elif var=='4':
                raw_str=input("Report your problem INFRASTRUCTURE SERVICES related issue : ")
            elif var=='5':
                raw_str=input("Report your problem DOCUMENT/RECORD MAINTENANCE related issue : ")
            else:
                raw_str=input("Report your problem other than above mentioned : ")
            return raw_str
def runProgramToRepeat():
    keepRepeating = 1
    while keepRepeating:
        keepRepeating = programToRepeat()
def programToRepeat():
    again = input("Do you want to Submit another complaint(ANSWER IN FORM OF YES OR NO):- ")
    if again == "yes" or again=="YES" :
        ask=input(" ARE YOU ALREADY SIGNED IN ?")
        if ask=="YES" or ask=="yes":
            options()
def insert():
    mycur.execute(f'INSERT INTO Applicants_info VALUES("{User_id}","{password}","{user_nme}","{age}","{contact_no}","{address}","{Email_id}");')
    mycur.execute(f'SELECT * FROM Applicants_info;')
    for m in mycur:
        print(m)
def confirm(user_id,Password):

    '''mycur.execute(f'ALTER TABLE Applicants_info MODIFY Contact_no BIGINT;')

    mycur.execute(f'INSERT INTO Applicants_info VALUES("D17H","Dan17ish","Danish",17,87654329,"Chandigarh","Da12@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("F40N","Far40an","Faran",40,876543219,"Chandigarh","fa12@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("A21H","At21ish","Atish",21,987654321,"Jalandhar Model Town H.no.-1711","At21@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("S24A","San24aya","Sanaya",24,942764321,"Opp. of ITI street no.-40 H.no.-652 ,Hsp","San@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("N23A","Nai23ra","Naira",23,839765432,"Kapurthala","Naira@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("A26N","Am26man","Amman",26,305643213,"Ropar","Amman26@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("A21A","Ae21ena","Aeena",21,673241569,"Pathankot","Ae21@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("Z31A","Zo31ya","Zoya",31,7382965401,"Ludhiana","Zoya@gmail.com")')
    mycur.execute(f'INSERT INTO Applicants_info VALUES("T20N","Ta20run","Tarun",20,6353210928,"Patiala","Tarun@gmail.com")')'''
    

    for k in mycur:
        print(k)
    
        
    '''if (user_id in m  and Password in m)or (user_id in i and Password in i):
                mycur.execute(f'SELECT * FROM Applicants_info WHERE (User_Id="{user_id}" and Password="{Password}")')
                for data in mycur:
                    print(data)
                confirmation=input(" IS IT YOUR DATA ? ")
                if confirmation == "YES" or  confirmation=="yes":
                        sign=" YOU ARE SIGNED IN "
                        print(sign)
                        con=input(" DO YOU WANT TO CONTINUE ")
                        if con == 'yes'or con== 'YES':
                            print(options())
                            print(runProgramToRepeat())
                            print(programToRepeat())
                        else:
                            return(" THANKYOU FOR YOUR RESPONSE ")
                elif confirmation == "no" or confirmation== "NO ":
                        print(user_data())
                        #data insert karna table '''
    (user_data())
    insert()
    

'''sign=" YOU ARE SIGNED IN "
                        print(sign)
                        con=input(" DO YOU WANT TO CONTINUE ")
                        if con== 'yes'or con== 'YES':
                            print(options())
                            print(runProgramToRepeat())
                            print(programToRepeat())
                        else:
                            return(" THANKYOU FOR YOUR RESPONSE ")
            else:
                fail=" INVALID INFORMATION , ENTER VALID  INFORMATION "
                print(fail)
                print(user_data())
                #add to table 
                sign=" YOU ARE SIGNED IN "
                print(sign)
                con=input(" DO YOU WANT TO CONTINUE ")
                if con== 'yes'or con== 'YES':
                    print(options())
                    print(runProgramToRepeat())
                    print(programToRepeat())
                else: 
                    return(" THANKYOU FOR YOUR RESPONSE ")'''
user_id=input(" ENTER YOUR USER ID :")
import maskpass
pwd=maskpass.askpass(mask=" ")
Password=pwd
print(confirm(user_id,Password))