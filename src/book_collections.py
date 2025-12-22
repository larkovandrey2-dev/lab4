from collections import UserList, UserDict


class BookCollection:
    """Пользовательская списочная коллекция книг, реализованная через композицию с UserList."""
    def __init__(self, initial_data = None):
        if initial_data:
            self.books = UserList(initial_data)
        else:
            self.books = UserList()
    def add_book(self, book):
        """Добавляет книгу в конец коллекции."""
        self.books.append(book)
    def remove_book(self, book):
        """Удаляет книгу из коллекции, если она там присутствует."""
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
        """Возвращает элемент по индексу или новую коллекцию при срезе."""
        if isinstance(index, slice):
            subset = self.books[index]
            return BookCollection(subset)
        return self.books[index]
    def __repr__(self):
        return f"BookCollection: {self.books}"
class IndexDict:
    """Пользовательская словарная коллекция для индексации книг по ISBN, автору и году."""
    def __init__(self):
        self.isbn = UserDict()
        self.authors = UserDict()
        self.years = UserDict()
    def add_book(self, book):
        """Обновляет все индексы при добавлении книги."""
        self.isbn[book.isbn] = book
        if book.author not in self.authors:
            self.authors[book.author] = BookCollection()
        self.authors[book.author].add_book(book)
        if book.year not in self.years:
            self.years[book.year] = BookCollection()
        self.years[book.year].add_book(book)
    def remove_book(self, book):
        """Удаляет книгу из всех индексов и очищает пустые записи."""
        if book.isbn not in self.isbn:
            return f"The book {book} is not in the collection"
        del self.isbn[book.isbn]
        if book.author in self.authors:
            self.authors[book.author].remove_book(book)
            if len(self.authors[book.author]) == 0:
                del self.authors[book.author]
        if book.year in self.years:
            self.years[book.year].remove_book(book)
            if len(self.years[book.year]) == 0:
                del self.years[book.year]
    def search_by_author(self, author):
        """Возвращает коллекцию книг указанного автора."""
        if author in self.authors:
            return self.authors[author]
        return BookCollection()
    def search_by_year(self, year):
        """Возвращает коллекцию книг за указанный год."""
        if year in self.years:
            return self.years[year]
        return BookCollection()
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
