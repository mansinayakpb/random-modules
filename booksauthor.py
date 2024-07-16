def detail_of_books():
    """Collects details about books and returns a list of dictionaries containing book information."""

    books = []

    while True:
        book_name = input("Enter book name: ")
        author_name = input("Enter author name: ")
        book_genre = input("Enter book genre: ")
        book_published_date = input("Enter book published date: ")
        books.append(
            {
                "book name": book_name,
                "author name": author_name,
                "book genre": book_genre,
                "book published date": book_published_date,
            }
        )

        more = input("Do you want to add more books? (y/n): ")
        if more != "y":
            break
    return books


book_collection = detail_of_books()

# Convert the list of books to the desired dictionary format
formatted_books = {
    book["book name"]: {
        "name": book["author name"],
        "book genre": book["book genre"],
        "book published date": book["book published date"],
    }
    for book in book_collection
}
print(formatted_books)
