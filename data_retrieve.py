from discount_calculation import Discount
from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.customer_data_save
class Data_retrieve():
    def data_from_db(mid_json,query):
        discount = 0
        bill = 0
        for i in range(len(mid_json['medicine'])):
            total_medicines = 0
            count = 0
            retrieve_previous_data = db.customer_data_save.find(query)
            for j in retrieve_previous_data:
                count = count + 1
                for k in range(len(j['medicine'])):
                    if mid_json['medicine'][i][0] == j['medicine'][k][0]:
                        total_medicines = total_medicines + int(j['medicine'][k][1])
            discount = Discount.discount(mid_json,total_medicines, count)
            bill = bill + int(mid_json['medicine'][i][1])*int(mid_json['medicine'][i][2])*(100-discount)/100
            print("billlll",bill)
            print("discount for ", mid_json['medicine'][i][0], discount)
        print("total bill",round(bill, 2))
        return bill