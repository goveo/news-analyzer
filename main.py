# import requests
from database import database

if __name__ == '__main__':
    db = database.connect()
    print("database connected")
    #
    # item_id = db["news"].insert_one({
    #     "text": "text"
    # }).inserted_id
    # print(item_id)

    data = db["news"].find_one({"_id": "5ce08b0d197b1e6b6a57a50b"})
    print("data :{}".format(data))

    # print("all data:")
    # data = db["news"].find()
    # for obj in data:
    #     print(obj)
