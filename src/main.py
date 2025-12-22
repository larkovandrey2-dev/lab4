from src.book import Library, PaperBook, EBook, Book
import random


TITLES_ADJ = ["Hidden", "Silent", "Broken", "Dark", "Golden", "Eternal", "Lost", "Cyber"]
TITLES_NOUN = ["Forest", "Empire", "Code", "Soul", "Star", "Dream", "Algorithm", "Python"]
AUTHORS = ["Pushkin", "Tolstoy", "Orwell", "King", "Rowling", "Gibson", "Knuth"]
GENRES = ["Fiction", "Sci-Fi", "Fantasy", "History", "Education", "Thriller"]


def generate_random_book() -> Book:
    """
    Генерирует случайный объект книги (PaperBook или EBook)
    со случайными атрибутами.
    """
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
    """
    Запускает псевдослучайную симуляцию работы библиотеки.
    :param steps: Количество шагов (событий) симуляции.
    :param seed: Зерно генератора случайных чисел для воспроизводимости результатов.
    """
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
