class Book:
    def __init__(self, title, author, status = 'AVAILABLE'):
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f'({self.status}) - {self.title}, By {self.author}'

class Library:
    def __init__(self):
        self.books = []

    def library_list(self, status_filter = None):
        print()
        for i, book in enumerate(self.books, start= 1):
            if not status_filter or book.status == status_filter:
                print(f'{i}. {book}')
        print()

    def check_out(self):
        while True:
            print()
            available_books = [book for book in self.books if book.status == 'AVAILABLE']
            if len(available_books) == 0:
                print('No Books Available.\nReturning to Menu...\n')
                return
            for i, book in enumerate(available_books, start= 1):
                print(f'{i}. {book}')
            print()

            print('Enter Book Title to Check Out, (Q) to Quit.')
            book_input = input('Title: ')
            if book_input.lower() == 'q':
                print('Returning to Menu...\n')
                return
            found = False
            for i, book in enumerate(available_books, start= 1):
                if book_input.lower() == book.title.lower():
                    found = True
                    print(f'\n({book.status}) - {book.title}, By {book.author}\n')
                    while True:
                        choice = input('Check Out? (Y/N): ')
                        if choice.lower() == 'y':
                            book.status = 'UNAVAILABLE'
                            print(f'Checked Out: {book.title}, By {book.author}')
                            break
                        elif choice.lower() == 'n':
                            break
            if not found:
                print(f"'{book_input}' is Unavailable or Does Not Exist.")
                continue


    def return_book(self):
        while True:
            print()
            unavailable_books = [book for book in self.books if book.status == 'UNAVAILABLE']
            if len(unavailable_books) == 0:
                print(f"No Books Returnable.\nReturning to Menu...\n")
                return
            for i, book in enumerate(unavailable_books, start= 1):
                print(f'{i}. {book}')

            print('\nEnter Book Title to Return, (Q) to Quit.')
            book_choice = input('Title: ')
            if book_choice.lower() == 'q':
                print('Returning to Menu...\n')
                return
            found = False
            for book in unavailable_books:
                if book_choice.lower() == book.title.lower():
                    found = True
                    print(f'\n{book}\n')
                    while True:
                        choice = input('Return This Book? (Y/N): ')
                        if choice.lower() == 'y':
                            book.status = 'AVAILABLE'
                            print(f'{book.title}, By {book.author} Returned')
                            break
                        elif choice.lower() == 'n':
                            break
            if not found:
                print(f"'{book_choice}' is Not Currently Checked Out or Does Not Exist.")
                continue

    def add_to_database(self):
        book_count = int(input('How many books to add?: '))
        print()
        for count in range(book_count):
           print(f'- Book {count + 1} -')
           book = Book(input('Enter Book Title: '), input('Enter Author: '))
           self.books.append(book)
           print()

library = Library()

while True:
    print('(1) Check Library Status, (2) Check Out Book, (3) Return Book, (4) Add to Database, (5) Quit.')
    check = int(input('Enter Number: '))
    if check not in list(range(1,6)):
        continue
    elif check == 1:
        if len(library.books) == 0:
            print('DATABASE EMPTY\n')
            continue
        library.library_list()
    elif check == 2:
        if len(library.books) == 0:
            print('DATABASE EMPTY\n')
            continue
        library.check_out()
    elif check == 3:
        if len(library.books) == 0:
            print('DATABASE EMPTY\n')
            continue
        library.return_book()
    elif check == 4:
        library.add_to_database()
    elif check == 5:
        break