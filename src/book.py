from collections import UserDict, UserList

class Book:
    """Базовый класс, описывающий книгу с основными атрибутами."""
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn
    def __repr__(self):
        return f"Book: {self.title}, {self.author}, {self.year}, {self.genre}, {self.isbn}"
class PaperBook(Book):
    """Класс для бумажных книг, добавляет атрибут веса."""
    def __init__(self, title, author, year, genre, isbn, weight):
        super().__init__(title,author,year,genre,isbn)
        self.weight = weight
    def __repr__(self):
        return f"Paper book: {self.title}, {self.author}, {self.year}, {self.genre}, {self.weight}, {self.isbn}"
class EBook(Book):
    """Класс для электронных книг, добавляет размер файла и формат."""
    def __init__(self, title, author, year, genre, isbn, size, format):
        super().__init__(title,author,year,genre,isbn)
        self.size = size
        self.format = format
    def __repr__(self):
        return f"Ebook: {self.title}, {self.author}, {self.year}, {self.genre}, {self.size}, {self.format}, {self.isbn}"


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

class Library:
    """Главный класс библиотеки, объединяющий хранение и индексацию."""
    def __init__(self):
        self.books = BookCollection()
        self.index_dict = IndexDict()
    def add_book(self, book):
        """Добавляет книгу одновременно в хранилище и в индексы."""
        self.books.add_book(book)
        self.index_dict.add_book(book)
    def remove_book(self, book):
        """Удаляет книгу из хранилища и индексов."""
        self.books.remove_book(book)
        self.index_dict.remove_book(book)
    def search_by_author(self, author):
        """Поиск книг по автору через индекс."""
        return self.index_dict.search_by_author(author)
    def search_by_year(self, year):
        """Поиск книг по году через индекс."""
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
