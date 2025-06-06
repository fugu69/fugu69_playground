# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}" #by default returns object's adress in memory

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author #by default return False

    def __lt__(self, other):    #by default throws an error
        return self.num_pages < other.num_pages

    def __gt__(self, other):    #by default throws an error
        return self.num_pages > other.num_pages

    def __add__(self, other):    #by default throws an error
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):    #by default throws an error
        return keyword in self.title or self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "length":
            return self.num_pages
        else:
            return "Not found"
    

book1 = Book("The Hobbit", "J.R.R. Talkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Hobbit", "J.R.R. Talkien", 310)

print(book1)            #by default prints object's adress in memory
print(book1 == book3)   #by default prints False
print(book2 < book1)    #by default prints error
print(book2 > book1)    #by default prints error
print(book2 + book1)    #by default prints error
print("Hobbit" in book1)    #by default prints error
print(book1["author"])    #by default prints error
