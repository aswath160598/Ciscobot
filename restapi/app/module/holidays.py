from flask import jsonify
import mysql.connector,json


user= "root"#parser.get('dblogin_detail', 'username')
password= "password123"#parser.get('dblogin_detail', 'password')
database= "bot" #parser.get('dblogin_detail', 'database')
host= "db" #parser.get('dblogin_detail', 'host')



def listhelpdeskemployees():
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute('SELECT empname,emailid,contact from helpdesk')
    myresult = mycursor.fetchall()

    mydict1={}
    for x in myresult:
        mydict1[x[0]]=(x[1],x[2])
    return jsonify(mydict1)

def listfloaters():
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute('SELECT DATE_FORMAT(occasion_Date, "%m-%d-%Y"),occasion from holiday where floater=1 ORDER BY occasion_Date')
    myresult = mycursor.fetchall()

    mydict={}
    for x in myresult:
        mydict[x[1]]=x[0]
    return jsonify(mydict)


def filter(month_filter):
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mycursor = mydb.cursor(buffered=True)
    month_filter = month_filter.upper()
    query='select occasion_Date,occasion from holiday where upper(month)=? and floater=1'
    mycursor.execute(query,(month_filter,))
    myresult=mycursor.fetchall()
    return jsonify(myresult)

def listholidays():
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute('SELECT DATE_FORMAT(occasion_Date, "%m-%d-%Y"),occasion from holiday where floater=0 ORDER BY occasion_Date')
    myresult = mycursor.fetchall()

    mydict={}
    for x in myresult:
        mydict[x[1]]=x[0]
    return jsonify(mydict)