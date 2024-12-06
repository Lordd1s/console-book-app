import os
import json
from typing import List, Dict, Optional, Callable


class Book:
    def __init__(self, file_path: str = "library.json"):
        self.file_path: str = file_path
        self.status: dict = {
            "IN_STOCK": "В наличии",
            "ISSUED": "Выдана"
        }

    def _file_exists(self) -> bool:  # check file exists
        return os.path.exists(self.file_path)

    def _read_file(self) -> List[Dict]:
        # reading file
        if not self._file_exists():
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

    def _write_file(self, data: List[Dict]) -> None:  # write to json
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Add book
        :param title: name of the book
        :param author: author name
        :param year: year
        :return: None! returns message from print()
        """
        if not title or not author or not year:
            raise ValueError(f"Invalid value: {title}, {author}, {year}")

        books: List[Dict] = self._read_file()
        max_id: int = max((book.get("id", 0) for book in books), default=0)  # get last id

        book = {
            "id": max_id + 1,
            "title": title,
            "author": author,
            "year": year,
            "status": self.status["IN_STOCK"]
        }

        books.append(book)
        self._write_file(books)


    def view_all_books(self) -> Optional[List[Dict]]:
        """
        All books!
        :return:
        """
        books: List[Dict] = self._read_file()
        if not books:
            print("Library is empty.")
            return None

        return books

    def delete_book(self, book_id: int) -> None:
        books: List[Dict] = self._read_file()
        for idx, book in enumerate(books):
            if book.get("id") == book_id:
                del books[idx]
                self._write_file(books)
                print("Book successfully deleted.")
                return

        print(f"No book found with ID {book_id}.")

    def search_book(self, query: str) -> List[Dict]:
        """
        search book in fields (title, author, year).

        :param query: query for search
        :return: List of found books.
        """
        books: List[Dict] = self._read_file()

        results: List[Dict] = [
            book for book in books
            if any(
                query.lower() in str(book[field]).lower()  # Checking query in field
                for field in {"title", "author", "year"}  # Fields
            )
        ]

        if not results:
            print(f"No books found for query '{query}'.")
            return []

        return results

    def update_status(self, book_id: int, status: str) -> None:
        """
        Status update
        :param book_id: id of book
        :param status: status string
        :return: None! returns info about success or fail print()
        """
        if status not in self.status.values():
            raise ValueError(f"Invalid status: {status}")

        books: List[Dict] = self._read_file()
        for book in books:
            if book.get("id") == book_id:
                book["status"] = status
                self._write_file(books)
                print(f"Book status updated to '{status}'.")
                return

        print(f"No book found with ID {book_id}.")


class BookManager:
    def __init__(self):
        self.book = Book()

    def add_book(self):
        print('Write a "title", "author", "year" to add a new book!')
        try:
            title = input("Book name: ")
            author = input("Author name: ")
            year = input("Year: ")
            self.book.add_book(title, author, year)
            print('Book successfully added.')
        except ValueError:
            print("Invalid input. Please provide correct data like: 'Art of masterpiece' John Doe 2000")

    def delete_book(self):
        try:
            book_id = int(input('Please input ID of book to delete: '))
            self.book.delete_book(book_id)
        except ValueError:
            print('Invalid input. Please provide a numeric ID.')

    def search_book(self):
        query = input("Please type author name, book name, or year: ")
        result = self.book.search_book(query=query)
        if result:
            for book in result:
                print(
                    f"ID: {book['id']}\n"
                    f"Title: {book['title']}\n"
                    f"Author: {book['author']}\n"
                    f"Year: {book['year']}\n"
                    f"Status: {book['status']}\n"
                    "----------------------"
                )
        else:
            print('No matching books found.')

    def view_all_books(self):
        books = self.book.view_all_books()
        if books:
            for book in books:
                print(
                    f"ID: {book['id']}\n"
                    f"Title: {book['title']}\n"
                    f"Author: {book['author']}\n"
                    f"Year: {book['year']}\n"
                    f"Status: {book['status']}\n"
                    "----------------------"
                )
        else:
            print('No books in the library.')

    def update_book_status(self):
        try:
            book_id = int(input('Please input ID of book to update status: '))
            print('Choose status (Enter a number):')
            print('[0] IN STOCK')
            print('[1] ISSUED')
            status_choice = int(input())
            if status_choice == 0:
                self.book.update_status(book_id, 'В наличии')
            elif status_choice == 1:
                self.book.update_status(book_id, 'Выдана')
            else:
                print('Invalid status choice.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')
