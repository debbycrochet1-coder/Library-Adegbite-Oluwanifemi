
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"You have borrowed '{self.title}'.")

    def return_book(self):
        self.is_borrowed = False
        print(f"You have returned '{self.title}'.")

# Create 3 Book objects
book1 = Book("Things Fall Apart", "Chinua Achebe")
book2 = Book("The Lion and the Jewel", "Wole Soyinka")
book3 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie")

# Borrow the books
book1.borrow()
book2.borrow()
book3.borrow()

# Return the books
book1.return_book()
book2.return_book()
book3.return_book()

# Display the availability of each book
print("\nBook Availability:")

for book in [book1, book2, book3]:
    if book.is_borrowed:
        status = "Borrowed"
    else:
        status = "Available"

    print(f"{book.title} by {book.author}: {status}")
