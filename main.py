# import requests
import database

if __name__ == '__main__':
    db = database.connect_db()
    # print("database connected")

    item_id = db["news"].insert_one({
        "text": "sampletext"
    }).inserted_id

    print(item_id)
    data = db["news"].find_one({"text":"sampletext"})
    print("data :{}".format(data["text"]))
