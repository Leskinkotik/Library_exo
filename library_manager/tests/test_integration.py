import unittest
import sys
import os

# Добавляем путь к библиотеке в sys.path, чтобы модули могли быть импортированы
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../library')))

from book import Book
from library import Library

class TestIntegration(unittest.TestCase):
    def test_library_integration(self):
        library = Library()
        book1 = Book("Title1", "Author1")
        book2 = Book("Title2", "Author2")

        library.add_book(book1)
        library.add_book(book2)

        self.assertIn(book1, library.books)
        self.assertIn(book2, library.books)

        library.remove_book(book1)
        self.assertNotIn(book1, library.books)

        found_book = library.find_book_by_title("Title2")
        self.assertEqual(found_book, book2)

if __name__ == '__main__':
    unittest.main()