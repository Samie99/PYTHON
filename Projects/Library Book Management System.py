class Book:
    def __init__(self, title, author, status = 'AVAILABLE'):
        self.title = title
        self.author = author
        self.status = status

class Library:
    def __init__(self):
        self.books = []

    def library_status(self):
        count = 0
        print()
        for book_dict in self.books:
            count += 1
            print(f'{count}. ({book_dict['Status']}) - {book_dict['Title']}, By {book_dict['Author']}')
        print()

    def check_out(self):
        count = 0
        print()
        for book_dict in self.books:
            if book_dict['Status'] == 'AVAILABLE':
                count += 1
                print(f'{count}. ({book_dict['Status']}) - {book_dict['Title']}, By {book_dict['Author']}')
        if count == 0:
            print('No Books Available.\n')
            return
        print()
        while True:
            count = 0
            print('Enter Book Title to Check Out, (Q) to Quit.')
            book_choice = input('Title (case sensitive): ')
            print()
            for book_dict in self.books:
                if book_choice == book_dict['Title'] and book_dict['Status'] == 'AVAILABLE':
                    count += 1
                    print(f'({book_dict['Status']}) - {book_dict['Title']}, By {book_dict['Author']}\n')
                    while True:
                        choice = input('Check Out? (Y/N): ')
                        if choice == 'Y':
                            book_dict['Status'] = 'UNAVAILABLE'
                            print(f'Checked Out: {book_dict['Title']}, By {book_dict['Author']}\n')
                            break
                        elif choice == 'N':
                            print()
                            break

            if book_choice == 'Q':
                print()
                return
            if count == 0:
                print('Invalid Book Title\n')
                continue

    def return_book(self):
        count = 0
        print()
        for book_dict in self.books:
            if book_dict['Status'] == 'UNAVAILABLE':
                count += 1
                print(f'{count}. ({book_dict['Status']}) - {book_dict['Title']}, By {book_dict['Author']}')
        if count == 0:
            print('No Books Returnable.\n')
            return
        while True:
            count = 0
            print('\nEnter Book Title to Return, (Q) to Quit.')
            book_choice = input('Title (case sensitive): ')
            for book_dict in self.books:
                if book_choice == book_dict['Title'] and book_dict['Status'] == 'UNAVAILABLE':
                    count += 1
                    print(f'\n({book_dict['Status']}) - {book_dict['Title']}, By {book_dict['Author']}\n')
                    while True:
                        choice = input('Return This Book? (Y/N): ')
                        if choice == 'Y':
                            book_dict['Status'] = 'AVAILABLE'
                            print(f'{book_dict['Title']}, By {book_dict['Author']} Returned')
                            break
                        elif choice == 'N':
                            break
            if book_choice == 'Q':
                print()
                return
            if count == 0:
                print('Invalid Book Title')
                continue

    def add_to_database(self, status = 'AVAILABLE'):
        book_count = int(input('How many books to add?: '))
        print()
        for count in range(book_count):
           print(f'- Book {count + 1} -')
           book = {'Title':input('Enter Book Title: '), 'Author':input('Enter Author: '), 'Status':status}
           print()
           self.books.append(book)
        if book_count <= 0:
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
        library.library_status()
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