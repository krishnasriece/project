import json
from flask import Flask, render_template
from data_retrieve import Data_retrieve
from send_to_database import Data_to_db
__author__ = 'krishna'
from pymongo import MongoClient
from flask import Flask, render_template, request
client = MongoClient(port=27017)

# define the database to use
db = client.customer_data_save
# define the flask app
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("check.html")
@app.route('/data', methods=["GET", "POST"])
def data():
    data = {}
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        phone = request.form['phone']
        gender = request.form['gender']
        num = request.form['txtNoOfRec']
        print("nummmmmmmmmmmmmmm",num)
        print(gender)
        mid_json = {"name": name, "age": age, "phone_number": phone, "email": email, "gender": gender}
        print("mid_json",mid_json)

        mid_json1 = Data_to_db.data_to_database(mid_json,num)

        query = {"name": mid_json1['name']}
        bill = Data_retrieve.data_from_db(mid_json1, query)
        mid_json["total bill"] = bill


        db.customer_data_save.insert_one(mid_json)


        return "Total bill is "+ str(round(bill, 2))
        #render_template("index.html")

@app.route('/getdata', methods=["GET", "POST"])
def getdata():
    query = {"Name": "Raj"}
    print(collection.find_one(query))
    return collection.find_one(query)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
    '''name = request.form['name']
    age = request.form['age']
    phone = request.form['phone']
    email = request.form['email']
    print("give the medicines list")
    mid_json = {"name": name, "age": age, "phone_number": phone, "email": email}
    mid_json1 = Data_to_db.data_to_database(mid_json)
    query = {"name" : mid_json1['name']}
    Data_retrieve.data_from_db(mid_json1,query)'''
    #app.run(host='0.0.0.0', port=4000)'''





















