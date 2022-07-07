class Book():
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"Book: '{self.title}' | Author: {self.author}"


class PaperBook(Book):
    def __init__(self, title, author, numPages) -> None:
        super().__init__(title, author)
        self.numPages = numPages

    def __str__(self) -> str:
        return f"Book: '{self.title}' | Author: {self.author} | Lists: {self.numPages}"


class EBook(Book):
    def __init__(self, title, author, size) -> None:
        super().__init__(title, author)
        self.size = size

    def __str__(self) -> str:
        return f"Book: '{self.title}' | Author: {self.author} | Size: {self.size}mb"


class Library:
    def __init__(self) -> None:
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def getSize(self):
        return len(self.books)


b0 = Book('The Odyssey', 'Homer')
b1 = EBook('The Odyssey', 'Homer', 2)
b2 = PaperBook('The Odyssey', 'Homer', 680)
print(f"{b0}\n{b1}\n{b2}")

addl = Library()
addl.addBook(b0)
addl.addBook(b1)
addl.addBook(b2)
print(addl.getSize())
