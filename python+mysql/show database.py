import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="username",passwd="your_pass",database="college")

mycursor=mydb.cursor()
mycursor.execute("select * from college")

result=mycursor.fetchall()

for i in result:
    print(i)

