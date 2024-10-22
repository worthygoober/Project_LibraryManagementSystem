import re

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_publication_date(self):
        return self.__publication_date
    
    def is_available(self):
        return self.__is_available
    
    def return_book(self):
        self.__is_available = True
    
    def borrow(self):
        if self.__is_available:
            self.__is_available = False
        else:
            raise Exception("Book is already borrowed.")

class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []
        # self.user_details = {}

    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id
    
    def get_borrowed_books(self):
        return self.__borrowed_books
    
    def borrow_book(self, title):
        self.__borrowed_books.append(title)

    def return_book(self, title):
        self.__borrowed_books.remove(title)

class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography
    
    def get_author_name(self):
        return self.__name
    
    def get_biography(self):
        return self.__biography
        
books = []
users = []
authors = []

def book_operations():
    while True:          
        print("\nBook Operations:")
        print("1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Return to menu")
        book_op_choice = input("Enter the operation to perform (1-6): ")
        if book_op_choice == "6":
            break
        try:
            if book_op_choice == "1":
                add_book()
            elif book_op_choice == "2":
                borrow_book()
            elif book_op_choice == "3":
                return_borrowed_book()
            elif book_op_choice == "4":
                search_for_book()
            elif book_op_choice == "5":
                display_all_books()
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")
        
def user_operations():      
    while True:
        print("\nUser Operations:")
        print("1. Add a new user\n2. View user details\n3. Display all users\n4. Return to menu")
        user_op_choice = input("Enter the operation number to perform (1-4): ")
        if user_op_choice == "4":
            break
        try:
            if user_op_choice == "1":
                add_user()
            elif user_op_choice == "2":
                display_user_details()
            elif user_op_choice == "3":
                display_all_users()
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author\n2. View author details\n3. Display all authors\n4. Return to menu")
        author_op_choice = input("Enter the operation number to perform (1-4): ")
        if author_op_choice == "4":
            break
        try:
            if author_op_choice == "1":
                add_author()
            elif author_op_choice == "2":
                display_author_details()
            elif author_op_choice == "3":
                display_all_authors()
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

def add_book():
    title = input("Enter the book's title: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the book's genre: ")
    publication_date = input("Enter the book's publication date (dd/mm/yyyy): ")
    books.append(Book(title, author, genre, publication_date))
    print(f"'{title}' has been added to the library.")

def borrow_book():
    title = input("Enter book title to borrow: ")
    for book in books:
        if book.get_title() == title:
            book.borrow()
            print(f"'{title}' has been checked out.")
            return
    print("Book unavailable or not found.")

def return_borrowed_book():
    title = input("Enter book title to return: ")
    for book in books:
        if book.get_title() == title:
            book.return_book()
            print(f"'{title}' has been returned.")
            return
    print("Invalid title or the book was not borrowed.")
    
def search_for_book():
    title = input("Enter book title to search: ")
    for book in books:
        if book.get_title() == title:
            availability = "Available" if book.is_available else "Borrowed"
            print(f"Title: {book.get_title()}\n    Author: {book.get_author()}\n    Genre: {book.get_genre()}\n    Publication Date: {book.get_publication_date()}\n    Availability: {availability}")
            return
    print("Book not found in library.")

def display_all_books():
    print("\nBook Catalog:")
    for book in books:
        availability = "Available" if book.is_available else "Borrowed"
        print(f"Title: {book.get_title()}\n    Author: {book.get_author()}\n    Status: {availability}")

def add_user():
    while True:
        name = input("Enter new user's name: ")
        if not is_valid_name():
            print("Invalid name. Please enter only letters and spaces.")
            continue
        library_id = input("Enter new user's library ID (must begin with 'L' and be followed by 4 digits): ")
        if not is_valid_library_id():
            print("Invalid ID. Library ID must begin with 'L' and be followed by 4 digits.")
            continue
        for user in users:
            if user.get_name() == name:
                print("User already exsists.")
                return
        users.append(User(name, library_id))
        print(f"New User '{name}' has been added with ID: {library_id}.")
    
def display_user_details():
    library_id = input("Enter the library ID for the user to display: ")
    for user in users:
        if user.get_library_id() == library_id:
            print(f"Name: {user.get_name()}\n    Library ID: {user.get_library_id()}\n    Borrowed Books: {user.get_borrowed_books()}")
            return
    print("User not found in library.")

def display_all_users():
    print("\nAll Library Users:")
    for user in users:
        print(f"Name: {user.get_name()}\n   Library ID: {user.get_library_id()}")

def add_author():
    author_name = input("Enter the author's name: ")
    author_biography = input("Enter the author's biography: ")
    authors.append(Author(author_name, author_biography))
    print(f"{author_name} has been added to the library.")

def display_author_details():
    author_name = input("Enter the author's name to display: ")
    for author in authors:
        if author.get_author_name() == author_name:
            print(f"Name: {author.get_author_name()}\n    Biography: {author.get_biography()}")
            return
    print("Author not found in library.")

def display_all_authors():
    print("\nAll Authors in Library:")
    for author in authors:
        print(f"Name: {author.get_author_name()}")

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-z]+$", name))

def is_valid_library_id(library_id):
    return bool(re.match(r"^L\d{4}+$", library_id))

while True:
    print("Welcome to the Library Management System!")
    print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
    choice = input("Enter the name of the Operations menu to access (book/user/author/quit): ")
    if choice.lower() == "quit":
        print("Thank you for using the Library Management System. The system is closing now.")
        break

    try:
        if choice.lower() == "book":
            book_operations()
        elif choice.lower() == "user":
            user_operations()
        elif choice.lower() == "author":
            author_operations()
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")