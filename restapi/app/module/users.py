from flask import jsonify
import mysql.connector


user= "root"#parser.get('dblogin_detail', 'username')
password= "password123"#parser.get('dblogin_detail', 'password')
database= "bot" #parser.get('dblogin_detail', 'database')
host= "db" #parser.get('dblogin_detail', 'host')

def registered(data):
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("SELECT * FROM registered")
    myresult = mycursor.fetchall()
    mydict={}
    for x in myresult:
        mydict[x[0]]=x[1]
    return(jsonify(mydict))

def register(data):
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    name=data['name']
    rid=data['id']
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("insert into registered VALUES (%s,%s)",(str(name),str(rid)))
    mydb.commit()
    mydb.close()
    return