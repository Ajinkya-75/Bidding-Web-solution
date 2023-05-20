import mysql.connector

db=mysql.connector.connect(host="localhost",
    user="root",
    password="root",
    database="mypython"
    )


cursor=db.cursor()

print("Database connectivity done.....")


