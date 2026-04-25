from utils import book
def add_book():
    book_name= input("enter the book name to add").strip().upper()
    book.append(book_name)
    print(f"Book-{book_name} added successsfully")

