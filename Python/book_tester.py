from book import Book

books = []
with open("books.txt") as file:
    for line in file:
        book_attributes = line.strip().split(",")
        title, author, genre = book_attributes
        new = Book(title, author, genre)
        books.append(new)
        print(new)
        
print(books[0].get_title())
print(books[0].get_author())
print(books[0].get_genre())
print(books[0].is_checked_out())

books[0].check_out()
print(books[0])
books[0].return_book()
print(books[0])
