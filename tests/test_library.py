import unittest
from src.book import Library, PaperBook, EBook

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.b1 = PaperBook("1984", "Orwell", 1949, "Dystopia", "ISBN-1", 300)
        self.b2 = EBook("Python Guide", "Guido", 2020, "Education", "ISBN-2", 5.5, "pdf")
        self.b3 = PaperBook("Animal Farm", "Orwell", 1945, "Satire", "ISBN-3", 150)
        self.library = Library()

    def test_collection_add_and_len(self):
        self.library.books.add_book(self.b1)
        self.library.books.add_book(self.b2)

        self.assertEqual(len(self.library.books), 2)
        self.assertEqual(self.library.books[0], self.b1)

    def test_collection_slicing(self):
        self.library.add_book(self.b1)
        self.library.add_book(self.b2)
        self.library.add_book(self.b3)
        sliced = self.library.books[0:2]

        self.assertIsInstance(sliced, list)
        self.assertEqual(len(sliced), 2)
        self.assertEqual(sliced[0].title, "1984")
        self.assertEqual(sliced[1].title, "Python Guide")

    def test_collection_iteration(self):
        self.library.add_book(self.b1)
        books_list = [book for book in self.library.books]
        self.assertEqual(books_list[0], self.b1)

    def test_index_add_and_search_isbn(self):
        self.library.add_book(self.b1)
        found_book = self.library["ISBN-1"]
        self.assertEqual(found_book, self.b1)

    def test_index_search_by_author(self):
        self.library.add_book(self.b1)
        self.library.add_book(self.b2)
        self.library.add_book(self.b3)

        orwell_books = self.library.search_by_author("Orwell")
        guido_books = self.library.search_by_author("Guido")

        self.assertEqual(len(orwell_books), 2)
        self.assertEqual(len(guido_books), 1)
        self.assertIn(self.b1, orwell_books)
        self.assertIn(self.b3, orwell_books)

    def test_index_search_by_year(self):
        self.library.add_book(self.b1)

        results = self.library.search_by_year(1949)
        self.assertEqual(results[0], self.b1)

        empty_results = self.library.search_by_year(2077)
        self.assertEqual(len(empty_results), 0)


    def test_remove_book_integrity(self):
        self.library.add_book(self.b1)
        self.library.add_book(self.b2)
        self.library.remove_book(self.b1)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0], self.b2)

        with self.assertRaises(KeyError):
            _ = self.library["ISBN-1"]

        orwell_books = self.library.search_by_author("Orwell")
        self.assertEqual(len(orwell_books), 0)

    def test_missing_isbn_error(self):
        with self.assertRaises(KeyError):
            _ = self.library["000-FAKE-ISBN"]


if __name__ == '__main__':
    unittest.main()
