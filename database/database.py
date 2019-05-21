from pymongo import MongoClient
import os

def connect(rs1="localhost:27001",
            rs2="localhost:27002",
            rs3="localhost:27003",
            rs_name="rs0",
            db_name="course-work"):
    # client = MongoClient([rs1, rs2, rs3], replicaset=rs_name)
    client = MongoClient("localhost:27100")
    return client[db_name]


def export_collection(db_name="course-work", collection="news", filepath="news.json", host="localhost:27100"):
    command = "mongoexport --db {} --collection {} --out {} --host {}".format(db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} exported to file {}".format(db_name, collection, filepath)


def import_collection(db_name="course-work", collection="news", filepath="news.json", host="localhost:27100"):
    command = "mongoimport --db {} --collection {} --file {} --host {}".format(db_name, collection, filepath, host)
    os.system(command)
    return "{}.collection {} imported to file {}".format(db_name, collection, filepath)
