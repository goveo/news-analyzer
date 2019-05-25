# import requests
from database import database
import analysis
import npyscreen

from gui import mainList



class MusiciansDBApp(npyscreen.NPSAppManaged):
    def __init__(self, *args, **keywords):
        super().__init__(*args, **keywords)
        self.db = database.connect()

    def onStart(self):
        self.addForm("MAIN", mainList.MainListDisplay, title='Main menu')

    def onCleanExit(self):
        # self.database.close()
        pass



if __name__ == '__main__':

    MyApp = MusiciansDBApp()
    MyApp.run()


    # analysis.get_popular_title_words()
    # analysis.get_time()
    # analysis.get_weekdays()
    # analysis.get_posting_stat()
    # analysis.print_month_news(year=2019, month=5)
    # analysis.print_day_news(year=2019, month=12, day=7)

    # print(database.export_collection())


    # print(database.import_collection(filepath="~/news.json"))