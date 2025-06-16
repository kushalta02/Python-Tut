import mysql.connector
mydb =mysql.connector.connect(
    host='localhost',
    user = 'root',
    password='khushipushi',
    database='Griv_sys'
)

User_id=input("name ")
Password=input("pass ")
mc=mydb.cursor()
#mc.execute("CREATE TABLE cants_Info (User_id VARCHAR(200),Password VARCHAR(100));")

#mc.execute(f'INSERT INTO cants_Info VALUES("{User_id}","{Password}");')
#mydb.commit()
mc.execute(" SELECT * FROM cants_Info;")
a=mc.fetchall()
r=""
for i in range(0,len(a)):
    us=a[i][0]
    pas=a[i][1]
    if us==User_id:
        if pas==Password:
            r=("log")
            print("oopps")
            
        else:
            r=("no pass")
            
        break
    else:
        r=("wrong")
        
print(r) log
if r== log: 
    print("yOu are login ")
    con()