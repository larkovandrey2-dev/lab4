from src.book import Book,EBook,PaperBook
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
