import unittest
import sys
import os

# Добавляем путь к библиотеке в sys.path, чтобы модули могли быть импортированы
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../library')))

from book import Book
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book("Title1", "Author1")
        self.book2 = Book("Title2", "Author2")

    def test_add_book(self):
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.books)

    def test_remove_book(self):
        self.library.add_book(self.book1)
        self.library.remove_book(self.book1)
        self.assertNotIn(self.book1, self.library.books)

    def test_remove_book_not_in_library(self):
        with self.assertRaises(ValueError):
            self.library.remove_book(self.book1)

    def test_find_book_by_title(self):
        self.library.add_book(self.book1)
        found_book = self.library.find_book_by_title("Title1")
        self.assertEqual(found_book, self.book1)

    def test_find_book_by_title_not_found(self):
        found_book = self.library.find_book_by_title("Nonexistent Title")
        self.assertIsNone(found_book)

    def test_list_books(self):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        book_list = self.library.list_books()
        self.assertIn(str(self.book1), book_list)
        self.assertIn(str(self.book2), book_list)

if __name__ == '__main__':
    unittest.main()
