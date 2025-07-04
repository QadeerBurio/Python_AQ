class Library:
    def __init__(self):
        self.no_books = 0  # Number of books
        self.books = []  # List to hold book titles

    def add_book(self, book_title):
        """Add a book to the library."""
        self.books.append(book_title)
        self.no_books += 1
        print(f'Book "{book_title}" added to the library.')

    def get_number_of_books(self):
        """Return the number of books in the library."""
        return self.no_books

    def print_all_books(self):
        """Print all books in the library."""
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(f'- {book}')
        else:
            print("No books in the library.")


def main():
    library = Library()  # Create a Library instance

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Print All Books")
        print("3. Get Number of Books")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            book_title = input("Enter the book title: ")
            library.add_book(book_title)

        elif choice == '2':
            library.print_all_books()

        elif choice == '3':
            print(f"Total number of books in the library: {library.get_number_of_books()}")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


# Run the main function to start the program
if __name__ == "__main__":
    main()
