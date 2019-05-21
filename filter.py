from database import database

db = database.connect()


def get_all_titles():
    return db.news.distinct("title")


def get_dates():
    return db.news.aggregate([
        {
            "$match": {
                "date": {
                    "$exists": True
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "date": 1
            }
        }
    ])


def get_all_news_dates():
    return db.news.aggregate([
        {
            "$match": {
                "date": {
                    "$exists": True
                }
            }
        },
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
                "_id.year": 1,
                "_id.day": 1
            }
        }
    ])


def get_news_per_month(year, month):
    return db.news.aggregate([
        {
            "$match": {
                "date": {
                    "$exists": True
                }
            }
        },
        {
            "$project": {
                "month": {
                    "$month": "$date"
                },
                "year": {
                    "$year": "$date"
                },
                "date": 1,
                "title": 1,
                "text": 1,
                "link": 1
            }
        },
        {
            "$match": {
                "month": month,
                "year": year
            }
        },
        {
            "$sort": {
                "date": 1
            }
        }
    ])



def get_news_per_day(year, month, day):
    return db.news.aggregate([
        {
            "$match": {
                "date": {
                    "$exists": True
                }
            }
        },
        {
            "$project": {
                "month": {
                    "$month": "$date"
                },
                "year": {
                    "$year": "$date"
                },
                "day": {
                    "$dayOfMonth": "$date"
                },
                "date": 1,
                "title": 1,
                "text": 1,
                "link": 1
            }
        },
        {
            "$match": {
                "day": day,
                "month": month,
                "year": year
            }
        },
        {
            "$sort": {
                "date": 1
            }
        }
    ])

#
# def drop_news():
#     db.news.remove()

# drop_news()
