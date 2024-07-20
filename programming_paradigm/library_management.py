class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = True
_books  = []
class Library:

    def add_book(self,book):
        _books.append(book)

    def  check_out_book(self,title):
        if title == _books:
            _books.remove()

    def return_book(self,title):
        if title != _books:
            _books.append()
    def list_available_books(self):
        return _books