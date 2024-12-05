import os
import json

from typing import List, Dict

from utils import search_util, get_book_by_id, path_exists


FILE_PATH: str = 'library.json'
STATUS = {
    'IN_STOCK': 'В наличии',
    'ISSUED': 'Выдана'
}
path = path_exists(FILE_PATH)


def add_book(title: str, author: str, year: int) -> None:
    if not title or not author or not year:
        raise ValueError(f'Invalid value: {title}, {author}, {year}')

    book: dict = {
        'title': title,
        'author': author,
        'year': year,
        'status': STATUS['IN_STOCK']
    }

    if path:
        with open(FILE_PATH, 'r+') as file:
            try:
                data: list[dict] = json.load(file)
            except json.JSONDecodeError:
                data: list = []
    else:
        data: list = []

    max_id: int = max((item.get('id', 0) for item in data), default=0)
    book['id'] = max_id + 1
    data.append(book)

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def view_all_books() -> List[Dict] | None:
    if path:
        with open(FILE_PATH, 'r') as file:
            try:
                data: List[Dict] = json.load(file)
                return data
            except json.JSONDecodeError:
                print("Library is empty")
                return None
    print("File does not exist")
    return None


def delete_book(book_id: int) -> None:
    if path:
        with open(FILE_PATH, 'r', encoding='UTF-8') as file:
            try:
                books: List[Dict] = json.load(file)
            except json.JSONDecodeError:
                print("File is corrupted or empty.")
                return

        for idx, itm in enumerate(books):
            if itm.get('id') == book_id:
                del books[idx]
                with open(FILE_PATH, 'w', encoding='UTF-8') as file:
                    json.dump(books, file, indent=4, ensure_ascii=False)
                print('Successfully deleted')
                return

        print(f"No book found with ID {book_id}.")
    else:
        print('File does not exist.')


def search_book(search_query: str | int) -> Dict | None:
    if search_query is None:
        raise ValueError('Invalid input')

    if path:
        try:
            with open(FILE_PATH, 'r') as file:
                books: List[Dict] = json.load(file)
                return search_util(books=books, search_obj=search_query)
        except json.JSONDecodeError:
            print('File empty')
    else:
        print("File does not exist.")
    return None


def update_book(book_id: int, new_data: Dict) -> None:
    if path:
        try:
            with open(FILE_PATH, 'r+', encoding='UTF-8') as file:
                try:
                    books: List[Dict] = json.load(file)
                except json.JSONDecodeError:
                    print("File is empty or corrupted.")
                    return

                book = get_book_by_id(books, book_id)
                if book is None:
                    print(f"No book found with ID {book_id}.")
                    return

                book.update(new_data)
                file.seek(0)
                json.dump(books, file, indent=4, ensure_ascii=False)
                file.truncate()
                print("Book successfully updated.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print('File does not exist')


def update_status(book_id: int, status: str) -> None:
    if path:
        try:
            with open(FILE_PATH, 'r+', encoding='UTF-8') as file:
                try:
                    books: List[Dict] = json.load(file)
                except json.JSONDecodeError:
                    print("File is empty or corrupted.")
                    return

                for book in books:
                    if book.get("id") == book_id:
                        book["status"] = status
                        file.seek(0)
                        json.dump(books, file, indent=4, ensure_ascii=False)
                        file.truncate()
                        print(f"Book status updated to '{status}'.")
                        return

                print(f"No book found with ID {book_id}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
