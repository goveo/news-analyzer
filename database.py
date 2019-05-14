from pymongo import MongoClient


def connect():
    client = MongoClient()
    return client['course-work']
