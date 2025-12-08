from collections import defaultdict

class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __repr__(self):
        return f"Book: {self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn}"
class PaperBook(Book):
    def __init__(self, title, author, year, genre, isbn, weight):
        super().__init__(title,author,year,genre,isbn)
        self.weight = weight
    def __repr__(self):
        return f"Paper book: {self.title}, {self.author}, {self.year}, {self.genre}, {self.weight}, {self.isbn}"
class EBook(Book):
    def __init__(self, title, author, year, genre, isbn, size, format):
        super().__init__(title,author,year,genre,isbn)
        self.size = size
        self.format = format
    def __repr__(self):
        return f"Ebook: {self.title}, {self.author}, {self.year}, {self.genre}, {self.size}, {self.format}, {self.isbn}"


class BookCollection:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"The book {book} is not in the collection")
    def __len__(self):
        return len(self.books)
    def __iter__(self):
        for book in self.books:
            yield book
    def __getitem__(self, index):
        return self.books[index]
    def __repr__(self):
        return f"BookCollection: {self.books}"
class IndexDict:
    def __init__(self):
        self.isbn = {}
        self.authors = defaultdict(list)
        self.years = defaultdict(list)
    def add_book(self, book):
        self.isbn[book.isbn] = book
        self.authors[book.author].append(book)
        self.years[book.year].append(book)
    def remove_book(self, book):
        if book.isbn not in self.isbn:
            return f"The book {book} is not in the collection"
        del self.isbn[book.isbn]
        self.authors[book.author].remove(book)
        self.years[book.year].remove(book)
    def search_by_author(self, author):
        return self.authors[author]
    def search_by_year(self, year):
        return self.years[year]
    def __getitem__(self, index):
        return self.isbn[index]
    def __iter__(self):
        for book in self.isbn:
            yield self.isbn[book]
    def __len__(self):
        return len(self.isbn)
    def __contains__(self, item):
        return item in self.isbn
    def __repr__(self):
        return f"Index: {self.isbn}"

class Library:
    def __init__(self):
        self.books = BookCollection()
        self.index_dict = IndexDict()
    def add_book(self, book):
        self.books.add_book(book)
        self.index_dict.add_book(book)
    def remove_book(self, book):
        self.books.remove_book(book)
        self.index_dict.remove_book(book)
    def search_by_author(self, author):
        return self.index_dict.search_by_author(author)
    def search_by_year(self, year):
        return self.index_dict.search_by_year(year)
    def __getitem__(self, index):
        return self.index_dict[index]
    def __len__(self):
        return len(self.index_dict)
    def __iter__(self):
        for book in self.index_dict:
            yield book
    def __repr__(self):
        return f"Library: {self.books}"
