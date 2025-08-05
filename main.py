from library import Library

lib = Library("City Library")

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        book = input("Enter book name to add: ")
        lib.add_book(book)

    elif choice == '2':
        lib.display_books()

    elif choice == '3':
        book = input("Enter book name to lend: ")
        user = input("Enter your name: ")
        lib.lend_book(book, user)

    elif choice == '4':
        book = input("Enter book name to return: ")
        lib.return_book(book)

    elif choice == '5':
        print("Thanks for using the Library system.")
        break

    else:
        print("Invalid option.")
