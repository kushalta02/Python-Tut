import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='khushipushi',
    database='griv_sys'
)
mycur=mydb.cursor(buffered=True)
def admin_features():
    raw=input(" ENTER PASSWORD ")
    if raw=='1234':
        print(" YOU ARE WELCOME ")
        opt=["1.STATUS UPDATE","2.REMINDER CHECK","3.INCHARGE/DUTY CHANGE"]
        for i in range(0,3):
            print(opt[i])
        var=input(" SELECT OPTION AS PER YOUR REQUIREMENT -- : " )
        if var=='1':
            s=input(' ENTER USER_ID TO BE UPDATED :' )
            k=input (' ENTER CURRENT STATUS: ')
            mycur.execute(f'update status_tab set status="{k}" where User_id="{s}";')
            mydb.commit()
            mycur.execute(f'select * from status_tab where User_id="{s}";')
            ak=mycur.fetchone()
            mycur.execute(f'show columns from status_tab;')
            am=mycur.fetchall()
            for k in range(0,len(am)):
                print(str(am[k][0]+'    '+' - '+'      '+str(ak[k])))
            
        elif var=='2':
            mycur.execute(f'select * from remind_me;')
            n=mycur.fetchall()
            mycur.execute(f'show columns from   remind_me;')
            o=mycur.fetchall()
            for u in n:
                print(str(o[u][0]+'    '+' - '+'      '+str(n[u])))
                #frst record only displayed
                
        else:
            c=int(input(" ENTER 1 FOR INCHARGE VARIATION AND 2 FOR VARIATION IN  ASSIGNED PROBLEM -"))
            if c==1:
                pro=input(" ENTER APPROPRIATE PROBLEM  ")
                inc=input(" ENTER NEW ADMIN :")
                mycur.execute(f'update admins_info set admins_name="{inc}" where leaders_duty="{pro}";')
                mydb.commit()
                mycur.execute(f'select * from admins_info where leader_duty="{pro}";')
                ak=mycur.fetchone()
                mycur.execute(f'show columns from admins_info;')
                am=mycur.fetchall()
                for k in range(0,len(am)):
                    print(str(am[k][0]+'    '+' - '+'      '+str(ak[k])))
            else:
                ad=input(" ENTER NAME OF ADMIN :")
                q=input(" ENTER NEW PROBLEM TO BE ASSIGNED :")
                mycur.execute(f'update admins_info set leaders_duty="{q}" where admins_name="{ad}";')
                mydb.commit()
                mycur.execute(f'select * from admins_info where admins_name="{ad}";')
                ak=mycur.fetchone()
                mycur.execute(f'show columns from admins_info;')
                am=mycur.fetchall()
                for k in range(0,len(am)):
                    print(str(am[k][0]+'    '+' - '+'      '+str(ak[k])))
    else:
        print(" YOU ARE NOT ADMIN ")
#admin_features()

print(" =========================== WELCOME TO ONLINE GRIEVANCE SYSTEM ==========================")
import getpass
import datetime
def user_data():
    print(" ENTER REQUIRED INFORMATION --")
    global User_id
    User_id = input(" ENTER YOUR USER ID : ")
    global password
    password=getpass.getpass(" ENTER YOUR PASSWORD :")
    global user_nme
    user_nme = input(" NAME :")
    global age
    age=int(input(" AGE :"))
    global contact_no
    contact_no=int(input(" CONTACT NO. "))
    global address
    address=input(" ADDRESS :")
    global Email_id
    Email_id=input(" ENTER EMAIL ADDRESS :")
    global date_reg
    date_reg=datetime.datetime.now()
def options():
    opt=["1.HEALTH AND SANITATION","2.SOCIAL PROBLEMS","3.ENVIRONMENT PROBLEMS","4.INFRASTRUCTURE SERVICES","5.DOCUMENT/RECORD MAINTENANCE PROBLEMS"]
    for i in range(0,5):
        print(opt[i])
    var=input(" SELECT APPROPRIATE CATEGORY  FOR YOUR GRIEVANCE -- : " )
    raw_str=' '
    if var=='1':
        raw_str=input(" Report your HEALTH AND SANITATION related issue : ")
        asi='MR.HENRY'
        print(" REPORTED ISSUE IS ASSIGNED TO-: ",asi)
        
    elif var=='2':
        raw_str=input(" Report your SOCIAL PROBLEMS related issue : ")
        asi='MRS.TISHANI DOSHI'
        print(" REPORTED ISSUE IS ASSIGNED TO-: ",asi)
    elif var=='3':
        raw_str=input(" Report your ENVIRONMENT related issue: ")
        asi='MR.ALPHONSE DAUDET'
        print(" REPORTED ISSUE IS ASSIGNED TO-: ",asi)
    elif var=='4':
        raw_str=input(" Report your INFRASTRUCTURE SERVICES related issue : ")
        asi='MR.FARADAY'
        print(" REPORTED ISSUE IS ASSIGNED TO-: ",asi)
    elif var=='5':
        raw_str=input(" Report your DOCUMENT/RECORD MAINTENANCE related issue : ")
        asi='MR.LENZ'
        print(" REPORTED ISSUE IS ASSIGNED TO-: ",asi)
    else:
        raw_str=input(" Report your problem other than above mentioned : ")
        asi='MRS.SNELL'
        print(" REPORTED ISSUE IS ASSIGNED TO-: ",asi)
    date_reg = datetime.datetime.now()
    mycur.execute(f'insert into status_tab values("{id}","{password}","{raw_str}","{asi}","{date_reg}","REGISTERED";')
    mydb.commit()
    return raw_str
    
def insert():
    mycur.execute(f'INSERT INTO Applicants_info VALUES("{User_id}","{password}","{user_nme}","{age}","{contact_no}","{address}","{Email_id}");')
    
    mydb.commit()
def programToRepeat():
    again = input("DO YOU WANT TO REGISTER MORE  GRIEVANCE :- ")
    if again.lower() == "yes" :
        ask=input(" ARE YOU ALREADY SIGNED IN ?")
        if ask.lower()=="yes":
            options()
            #table wala 
        else:
            user_data()
            insert()
            options()
    else:
        print(" - THANKYOU FOR YOUR RESPONSE - ")
def main(User_id,password):
   #------------------------------------------Exta new code start
   
   
    mycur.execute(f'SELECT * FROM Applicants_info where User_id="{id}";')
    record = mycur.fetchone()
    loggedIn=False
    showError=False
    message=""
    if record:
        if password == record[1]:
            loggedIn=True
        else:
            showError=True
            message="-----INCORRECT PASSWORD-----"
    else:
        showError=True
        message="-----INVALID USER_ID-----"
    
    if loggedIn:
        mycur.execute(f'select * from Applicants_info where User_id="{id}";')
        ak=mycur.fetchone()
        mycur.execute(f'show columns from Applicants_info;')
        am=mycur.fetchall()
        for k in range(0,len(am)):
            print(str(am[k][0]+'    '+' - '+'      '+str(ak[k])))
        con=input(" IS IT YOUR DATA ? ")
        if con.lower()=='yes':
            b=int(input(" ENTER 1 FOR STATUS ENQUIRY AND 2 FOR REGISTRING GRIVANCE: "))
            if b==1:
                mycur.execute(f'select  * status_tab where  User_id ="{id}";')
                ak=mycur.fetchone()
                mycur.execute(f'show columns from status_tab;')
                am=mycur.fetchall()
                for k in range(0,len(am)):
                    print(str(am[k][0]+'    '+' - '+'      '+str(ak[k]))) 
                vi=input(" DO YOU WANT TO SET A REMINDER ? ")
                if vi.lower()=='yes':
                    da=datetime.date(int(input(" ENTER REMINDER  DATE ")))
                    mycur.execute(f'insert into remind_me values("{id}","{password}","{da}");')
                    mydb.commit()
                    print(" REMINDER SET  ")
                else:
                    print(" THANKYOU FOR YOUR RESPONSE ")
            else:
                options()
                programToRepeat()
        else:
            user_data()
            insert()
            options()
            programToRepeat()
    
    if showError:
        print(message)
        user_data()
        insert()
        options()
        programToRepeat()           
    

   #------------------------------------------Exta new code end   
    
id=input(" ENTER YOUR USER ID -: ")
password=getpass.getpass(" ENTER YOUR PASSWORD ")
print(main(id,password))