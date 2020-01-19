from core.baseapp import BaseApp
from view.view_book import ViewBook

class MainApp(BaseApp):
    def __init__(self):
        self.books = []

if __name__ == "_ main__":
    app = MainApp()
    app.run()

class view(ViewBook):
    def __init__(self):
        vBook = ViewBook(self.book)
        bBook.list()

if __name__ == "__main__":
    app = MainApp()
    app.run()