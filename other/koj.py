import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='khushipushi',
    database='griv_sys'
)
mycur=mydb.cursor()

# print("cols ",am, len(am))

User_id = input(" ")
Password=input(" ")
mycur.execute(f'select * from Applicants_info where User_id="{User_id}" and Password="{Password}";')
ak=mycur.fetchone()
print("yes",ak)
mycur.execute(f'show columns from Applicants_info;')
am=mycur.fetchall()
# print(ak)

for k in range(0,len(am)):
    print(str(am[k][0]+' - '+str(ak[k])))
