from pymongo import MongoClient


def connect(rs1="localhost:27001",
            rs2="localhost:27002",
            rs3="localhost:27003",
            rs_name="rs0",
            db_name="course-work"):
    # client = MongoClient([rs1, rs2, rs3], replicaset=rs_name)
    client = MongoClient("localhost:27100")
    return client[db_name]