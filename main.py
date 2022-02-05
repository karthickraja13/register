import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="",database="file1")

cursor=conn.cursor()


select="select*from registeration"
cursor.execute(select)
recodes=cursor.fetchall()

print("detiles")
for x in recodes:
    print("id",x[0])
    print("name",x[1])
    print("email",x[2])
    print("password",x[3])
    print()
cursor.close()
conn.close()