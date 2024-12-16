

class BookNotFoundError(Exception):

    def __init__(self):
        super().__init__('Книга не найдена в библиотеке')


class Library:

    def __init__(self):
        self.books = set()


    def add_book(self, title):
        self.books.add(title)


    def remove_book(self, title):
        if title not in self.books:
            raise BookNotFoundError()

        self.books.remove(title)


    def list_books(self):
        return list(self.books)



import unittest

class TestLibrary(unittest.TestCase):


    def setUp(self):
        self.library = Library()


    def test_add_book(self):
        self.library.add_book("1997")
        self.assertIn("1997", self.library.list_books())


    def test_remove_book(self):
        self.library.add_book("Origin")
        self.library.remove_book("Origin")
        self.assertNotIn("Origin", self.library.list_books())


    def test_remove_nonexistent_book(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")


if __name__ == '__main__':
    unittest.main()
        
