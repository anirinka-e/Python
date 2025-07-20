from book import Book

library = [Book("Метель", "Пушкин"),
           Book("Бородино", "Лермонтов"),
           Book("Послушайте", "Маяковский")]

for i in library:
    print(f"{i.book_title} - {i.book_author}")
