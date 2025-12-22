
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
