import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="khushipushi",
  database='Griv_sys'
)
mycur=mydb.cursor()
mycur.execute(f'select * from  Users;')
n=mycur.fetchall()
print(n)