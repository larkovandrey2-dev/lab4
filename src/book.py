from collections import defaultdict
import random

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

TITLES_ADJ = ["Hidden", "Silent", "Broken", "Dark", "Golden", "Eternal", "Lost", "Cyber"]
TITLES_NOUN = ["Forest", "Empire", "Code", "Soul", "Star", "Dream", "Algorithm", "Python"]
AUTHORS = ["Pushkin", "Tolstoy", "Orwell", "King", "Rowling", "Gibson", "Knuth"]
GENRES = ["Fiction", "Sci-Fi", "Fantasy", "History", "Education", "Thriller"]


def generate_random_book() -> Book:
    title = f"{random.choice(TITLES_ADJ)} {random.choice(TITLES_NOUN)}"
    author = random.choice(AUTHORS)
    year = random.randint(1900, 2025)
    genre = random.choice(GENRES)
    isbn = f"978-{random.randint(1, 9)}-{random.randint(10000, 99999)}"
    if random.choice([True, False]):
        weight = random.randint(100, 1500)
        return PaperBook(title, author, year, genre, isbn, weight)
    else:
        file_size = round(random.uniform(0.5, 50.0), 2)
        format = random.choice(["pdf", "epub", "txt"])
        return EBook(title, author, year, genre, isbn, file_size,format)


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)
        print(f"ЗАПУСК СИМУЛЯЦИИ (Seed: {seed})")
    else:
        print("ЗАПУСК СИМУЛЯЦИИ (Random Seed)")

    library = Library()

    actions = ['add', 'remove', 'search_author', 'search_year', 'search_missing']

    for step in range(1, steps + 1):
        action = random.choice(actions)
        print(f"\n[Шаг {step}] Событие: {action.upper()}")

        if action == 'add':
            book = generate_random_book()
            library.add_book(book)
            print(f"  -> Добавлена: {book}")
            print(f"  -> Всего книг: {len(library)}")

        elif action == 'remove':
            if len(library) > 0:
                random_index = random.randint(0, len(library) - 1)
                victim_book = library.books[random_index]

                library.remove_book(victim_book)
                print(f"-> Удалена: {victim_book.title}")
            else:
                print("-> Ошибка: Нельзя удалить, библиотека пуста!")

        elif action == 'search_author':
            random_author = random.choice(AUTHORS)
            results = library.search_by_author(random_author)
            if results:
                print(f"-> Найдено {len(results)} книг автора {random_author}:")
                print(f"   Пример: {results[0].title}")
            else:
                print(f"-> Книг автора {random_author} не найдено.")

        elif action == 'search_year':
            random_year = random.randint(1990, 2025)
            results = library.search_by_year(random_year)

            if results:
                print(f"  -> Найдено {len(results)} книг за {random_year} год.")
            else:
                print(f"  -> В {random_year} году ничего не выходило.")

        elif action == 'search_missing':
            fake_isbn = "000-0-00000-000"
            try:
                book = library[fake_isbn]
                print(f"-> Найдена книга: {book}")
            except KeyError:
                print(f"-> Система корректно вернула ошибку (Книги {fake_isbn} нет).")
            except Exception as e:
                print(f"-> Неожиданная ошибка: {e}")

    print("\nСИМУЛЯЦИЯ ЗАВЕРШЕНА")
    print(f"Итого книг в библиотеке: {len(library)}")


if __name__ == "__main__":
    run_simulation()



