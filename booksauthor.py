def detail_of_books():
    books = {}

    while True:
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")
        book_genre = input("Enter book genre: ")
        book_published_date = input("Enter book published date: ")
        books[book_name] = {
            "name": author_name,
            "book genre": book_genre,
            "book published date": book_published_date,
        }

        more = input("Do you want to add more books? (y/n): ")
        if more != "y":
            break
    return books


book_collection = detail_of_books()
li = []
li.append(book_collection)
print(li)
