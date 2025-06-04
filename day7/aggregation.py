# Aggregation = Represents a relationships where one object (the whole, acts as a container)
#               contains references to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("New Your Public Library")

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Talkien")
book3 = Book("The colour of Magic", "Terry Pratchet")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(f"Welcome to {library.name}! List of available books:")
for book in library.list_books():
    print(book)
    print(type(book))

print(type(library.list_books()))
