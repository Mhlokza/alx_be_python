class Books:
    def __init__(self,title,author):
        self.title= title
        self.author= author
        self._is_checked_out=True

class Library(Books):
    _books =[]
    def add_book(self):
        self._books.append(book)

    def check_out_book(self,title):
        self._books.remove(title)

    def list_available_books(self):
        if self._books==self.title:
            self._books+=book
            print(f" Available books after checking out {self._books}")

    def return_book(self,title):
        if self._books != title:
            self._books+=book

