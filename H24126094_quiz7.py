library = {}

def add_book():
    try:
        title, genre, price = input("Enter the title, genre, and price of the book separated by a vertical bar '|': ").split('|')
        library[title.strip()] = {'genre': genre.strip(), 'price': float(price.strip())}
        print(f"The book '{title.strip()}' has been added.")
    except ValueError:
        print("Invalid input format. Please enter the title, genre, and price separated by a vertical bar '|'.")
    return True

def remove_book():
    title = input("Enter the title of the book you want to remove: ").strip()
    if title in library:
        del library[title]
        print(f"The book '{title}' has been removed.")
    else:
        print("Error: The book was not found.")

def get_book_information():
    title = input("Enter the title of the book: ").strip()
    if title in library:
        book = library[title]
        print(f"Title: {title}")
        print(f"Genre: {book['genre']}")
        print(f"Price: ${book['price']:.2f}")
    else:
        print("Error: The book was not found.")

def list_all_books():
    if library:
        for title in sorted(library.keys()):
            book = library[title]
            print(f"{title} ({book['genre']}, ${book['price']:.2f})")
    else:
        print("The library is empty.")

def list_books_by_genre():
    genre = input("Enter the genre: ").strip()
    books_in_genre = {title: book for title, book in library.items() if book['genre'] == genre}
    if books_in_genre:
        print(f"Listing all books in genre '{genre}':")
        for title in sorted(books_in_genre.keys()):
            book = books_in_genre[title]
            print(f"{title} ({book['genre']}, ${book['price']:.2f})")
    else:
        print(f"No books found in genre '{genre}'.")

while True:
    print("\nMenu")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Get book information")
    print("4. List all books")
    print("5. List books by genre")
    print("6. Quit")
    choice = input("Select an option (1-6): ").strip()
        
    if choice == '1':
        add_book()
        print("")
        list_all_books()
    elif choice == '2':
        remove_book()
        print("")
        list_all_books()
    elif choice == '3':
        get_book_information()
    elif choice == '4':
        list_all_books()
    elif choice == '5':
        list_books_by_genre()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please select a number between 1 and 6.")