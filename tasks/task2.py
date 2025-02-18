import logging
from abc import ABC, abstractmethod


log_formatter = logging.Formatter(
    "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s"
)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(log_formatter)

logger = logging.getLogger("library_logger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    def __init__(self):
        self.books = []

    @abstractmethod
    def add_book(self, title: str, author: str, year: str):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def add_book(self, title: str, author: str, year: str):
        self.books.append(Book(title, author, year))

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            logger.info(book)


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        self.library.add_book(title, author, year)

    def remove_book(self, title):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
