from pymongo import MongoClient
from time import sleep

def connect(url="mongodb://localhost:27001/", dbname="course-work"):
    print("connecting...")
    # client = MongoClient(url, replicaset='rs0')
    # client = MongoClient('mongodb://localhost:27001,localhost:27002/?replicaSet=rs0')
    client = MongoClient(['localhost:27001', 'localhost:27002', 'localhost:27003'], replicaset='rs0')
    # config = {'_id': 'rs0', 'members': [
    #     {'_id': 0, 'host': 'localhost:27001'},
    #     {'_id': 1, 'host': 'localhost:27002'}
    # ]}
    # client.admin.command("replSetInitiate", config)
    # dblist = client.list_database_names()
    # print(dblist)
    print("connected!")
    return client[dbname]
