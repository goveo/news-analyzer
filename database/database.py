from pymongo import MongoClient


def connect(url, dbname):
    client = MongoClient(url)
    # dblist = client.list_database_names()
    # print(dblist)
    return client[dbname]
