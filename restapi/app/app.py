from flask import Flask, request, jsonify, url_for
from flask_restful import Resource, Api

app= Flask(__name__)
api=Api(app)

import users
import holidays
import birthday

@app.route("/registered", methods=['POST'])
def registered():
    return(users.registered(request.form))

@app.route("/register", methods=['POST'])
def register():
    return(users.register(request.form))

@app.route("/listhelpdeskemployees",methods=['GET'])
def listhelpdeskemployees():
    if request.method=='GET':
        return(holidays.listhelpdeskemployees())

@app.route("/listfloaters",methods=['GET'])
def listfloaters():
    if request.method=='GET':
        return(holidays.listfloaters())


@app.route('/listfloaters/<month_filter>/filter', methods=['GET'])
def filter(month_filter):
    if request.method=='GET':
        return(holidays.filter())


@app.route("/listholidays",methods=['GET'])
def listholidays():
    if request.method=='GET':
        return(holidays.listholidays())

@app.route("/listbirthdays",methods=['GET'])
def listbirthdays():
    if request.method=='GET':
        return(birthday.listbirthdays())

@app.route("/upcomingbirthdays",methods=['GET'])
def upcomingbirthdays():
    if request.method=='GET':
        return(birthday.upcomingbirthdays())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')