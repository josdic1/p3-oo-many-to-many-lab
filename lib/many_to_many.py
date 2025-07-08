class Book:
    all = []

    def __init__(self, title):
        self._title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]
  
class Author:
    all = []

    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in Contract.all if c.author == self]

    def total_royalties(self):
        return sum(c.royalties for c in Contract.all if c.author == self)

    def sign_contract(self, book, date, total_royalties):
        return Contract(self, book, date, total_royalties)

     

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
           raise Exception("Author must be an author object")
        if not isinstance(book, Book):
           raise Exception("Book must be an book object")
        if not isinstance(date, str):
           raise Exception("Date must be a string")
        if not isinstance(royalties, int):
           raise Exception("Royalties must be an intefer")
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
       return self._author
    
    @property
    def book(self):
       return self._book

    @property
    def date(self):
       return self._date
    
    @property
    def royalties(self):
        return self._royalties
    
    @classmethod
    def contracts_by_date(cls, date):
       return [c for c in cls.all if c._date == date]

