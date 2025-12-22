import random
from src.library import Library
from src.helpers import generate_random_book

AUTHORS = ["Pushkin", "Tolstoy", "Orwell", "King", "Rowling", "Gibson", "Knuth"]

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
