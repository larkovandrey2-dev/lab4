from src.book_collections import BookCollection, IndexDict

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
