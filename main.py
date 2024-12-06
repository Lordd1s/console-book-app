import time

from crud import BookManager


def main():
    print('Welcome to the library app!')
    manager = BookManager()

    while True:
        print('\nPlease choose the operation:')
        print('1. Add a book')
        print('2. Delete a book')
        print('3. Search for a book')
        print('4. View all books')
        print('5. Update book status')
        print('0. Exit')

        try:
            operation = int(input())
            match operation:
                case 0:
                    print('Goodbye!')
                    break
                case 1:
                    manager.add_book()
                case 2:
                    manager.delete_book()
                case 3:
                    manager.search_book()
                case 4:
                    manager.view_all_books()
                case 5:
                    manager.update_book_status()
                case _:
                    print('Invalid choice. Please choose a valid option.')
        except ValueError:
            print('Invalid input. Please enter a number between 0 and 6.')

if __name__ == "__main__":
    main()
