from pymongo import MongoClient


def connect(url="mongodb://localhost:27017/", dbname="course-work"):
    client = MongoClient(url)
    # dblist = client.list_database_names()
    # print(dblist)
    return client[dbname]
