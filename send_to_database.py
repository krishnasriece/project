from pymongo import MongoClient
from flask import request
client = MongoClient(port=27017)
db = client.customer_data_save
class Data_to_db():
    def data_to_database(mid_json,num):
        medicine = []
        for i in range(1,int(num)+1):

            #inpu = input("enter medicine name")
            #if inpu == "0":
            #    break
            #quantity = input("enter quantity")
            #price = input("enter price of each medicine")
            med = []
            name = "txtFName"+str(i)
            print("request.form[name]")
            med.append(request.form[name])
            quantity = "txtq"+str(i)
            med.append(request.form[quantity])
            price = "txtp"+str(i)
            med.append(request.form[price])
            medicine.append(med)
            mid_json["medicine"] = medicine
        #db.student.insert_one(mid_json)
        print("mid_json_json",mid_json)
        return mid_json