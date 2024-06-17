import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../library')))

from book import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Title", "Author")
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")

    def test_book_str(self):
        book = Book("Title", "Author")
        self.assertEqual(str(book), "Title by Author")

if __name__ == '__main__':
    unittest.main()
