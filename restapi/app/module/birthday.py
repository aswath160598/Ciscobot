from flask import jsonify
import mysql.connector


user= "root"#parser.get('dblogin_detail', 'username')
password= "password123"#parser.get('dblogin_detail', 'password')
database= "bot" #parser.get('dblogin_detail', 'database')
host= "db" #parser.get('dblogin_detail', 'host')

def listemps():
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mydb.row_factory = dict_factory
    cur = mydb.cursor(buffered=True)
    all_emps = cur.execute('SELECT * FROM employee;').fetchall()

    return jsonify(all_emps)

def listbirthdays():
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor1 = mydb.cursor(buffered=True)
    mycursor.execute('SELECT e.NAMEEMP,e.managerid, e.dob, m.NAMEEMP FROM   employee e JOIN   employee m on e.managerid = m.empid')
    myresult = mycursor.fetchall()
    mydict={}
    for x in myresult:
        myresult1=[]
        man=x[1]
        mycursor1.execute('SELECT NAMEEMP from employee where managerid = ' + man + '')
        myresult1 = mycursor1.fetchall()
        n=[]
        for y in myresult1:
            am=str(y)
            le=len(am)
            am=am[2:le-3]
            n.append(am)
        n.remove(x[0])
        n.append(x[3])
        mydict[x[0]]=(x[2],str(n))
    return jsonify(mydict)


def upcomingbirthdays():
    mydb = mysql.connector.connect(
    host=str(host),
    user=str(user),
    passwd=str(password),
    database=str(database)
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor1 = mydb.cursor(buffered=True)

    mycursor.execute("SELECT NAMEEMP,managerid, dob FROM employee where DATE_FORMAT(dob, '%m-%d')=DATE_FORMAT('2020-08-27', '%m-%d')")
    myresult = mycursor.fetchall()
    mylist=[]
    for x in myresult:
        myresult1=[]
        man=x[1]
        mycursor1.execute('SELECT NAMEEMP from employee where managerid ="5001"')
        myresult1 = mycursor1.fetchall()
        for y in myresult1:
            mylist.append(y[0])
    return jsonify(mylist)