from database import database
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

def get_all_titles() -> []:
    db = database.connect()
    return db.news.distinct("title")

# return db.news.aggregate([
#         {
#             '$match': {
#                 "topic": {
#                     "$exists": True
#                 }
#             }
#         },
#         {"$project": {"_id": 0, "title": 1}},
#         {"$unwind": "$title"},
#         {"$group": {"_id": {"$toLower": "$title"}, "appears": {"$sum": 1}}},
#         {"$sort": {"title": 1}}
#     ])
