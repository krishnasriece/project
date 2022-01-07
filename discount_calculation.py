import math
class Discount():
    def discount(mid_json,total_medicines,count):
        if count == 0.0:
            discount = 0
        if total_medicines == 0:
            discount = 0
        if count != 0 and total_medicines != 0:
            print("total_medicines / count",total_medicines / count)
            discount = math.log(total_medicines / count, 10)
            if discount < 0:
                discount = 0
            if discount > 30:
                discount = 30
        return discount