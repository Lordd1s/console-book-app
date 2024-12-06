import os

from crud import Book


def test_book_class():
    test_file_path = "test_library.json"

    if os.path.exists(test_file_path):
        os.remove(test_file_path)


    book_manager = Book(file_path=test_file_path)


    book_manager.add_book("Test Title", "Test Author", "2024")
    books = book_manager._read_file()
    assert len(books) == 1, "The book was not added properly."
    assert books[0]["title"] == "Test Title", "The book title is incorrect."
    assert books[0]["author"] == "Test Author", "The book author is incorrect."
    assert books[0]["year"] == "2024", "The book year is incorrect."
    assert books[0]["status"] == "В наличии", "The book status is incorrect."


    all_books = book_manager.view_all_books()
    assert len(all_books) == 1, "View all books failed."


    results = book_manager.search_book("Test Title")
    assert len(results) == 1, "Search book failed."
    assert results[0]["title"] == "Test Title", "Search result is incorrect."


    book_manager.update_status(book_id=1, status="Выдана")
    updated_books = book_manager._read_file()
    assert updated_books[0]["status"] == "Выдана", "The book status was not updated."


    book_manager.delete_book(book_id=1)
    books_after_deletion = book_manager._read_file()
    assert len(books_after_deletion) == 0, "The book was not deleted properly."


    if os.path.exists(test_file_path):
        os.remove(test_file_path)

    print("All tests passed!")


if __name__ == "__main__":
    test_book_class()
