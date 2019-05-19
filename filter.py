from database import database

db = database.connect()


def get_all_titles():
    return db.news.distinct("title")


def get_dates():
    return db.news.aggregate([
        {
            '$sort': {
                'date': 1}
        },
        {
            "$project": {
                "_id": 0,
                "date": 1
            }
        }
    ])


def get_year_dates():
    return db.news.aggregate([
        {
            "$group": {
                "_id": {
                    "year": {
                        "$year": "$date"
                    },
                    "day": {
                        "$dayOfYear": "$date"
                    }
                },
                "count": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "_id.day": 1
            }
        }
    ])


def drop_news():
    db.news.remove()

# return db.news.aggregate([
#         {
#             '$match': {
#                 "topic": {
#                     "$exists": True
#           .      }
#             }
#         },
#         {"$project": {"_id": 0, "title": 1}},
#         {"$unwind": "$title"},
#         {"$group": {"_id": {"$toLower": "$title"}, "appears": {"$sum": 1}}},
#         {"$sort": {"title": 1}}
#     ])

# drop_news()