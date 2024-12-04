import time


def main():
    print('Welcome to library app!')
    time.sleep(0.5)
    while True:

        print('Please choose the operation: ')
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
                    ...
                case 2:
                    ...
                case 3:
                    ...
                case 4:
                    ...
        except ValueError:
            print('Invalid input. Please enter a number')


if __name__ == "__main__":
    main()
