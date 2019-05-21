# import requests
from database import database
import analysis

if __name__ == '__main__':
    db = database.connect()
    print("database connected")

    # analysis.get_popular_title_words()
    # analysis.get_time()
    # analysis.get_weekdays()
    # analysis.get_posting_stat()
    # analysis.print_month_news(year=2019, month=5)
    # analysis.print_day_news(year=2019, month=12, day=7)

    # print(database.export_collection())
    print(database.import_collection(filepath="news.json"))