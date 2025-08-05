class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.lend_data = {}

    def add_book(self, book):
        self.books.append(book)
        print(f'"{book}" added to the library.')

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Available Books:")
            for book in self.books:
                print(f"- {book}")

    def lend_book(self, book, user):
        if book in self.books and book not in self.lend_data:
            self.lend_data[book] = user
            print(f'"{book}" has been lent to {user}.')
        elif book in self.lend_data:
            print(f'"{book}" is already lent to {self.lend_data[book]}.')
        else:
            print(f'"{book}" is not in the library.')

    def return_book(self, book):
        if book in self.lend_data:
            self.lend_data.pop(book)
            print(f'"{book}" has been returned.')
        else:
            print(f'"{book}" was not lent.')
