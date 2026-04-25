from utils import book , issued_book
def return_book():
    book_name= input("enter the book name to return").strip().upper()
    if book_name in issued_book:
        issued_book.remove(book_name)
        book.append(book_name)
        print(f"Book - {book_name} returned successfully")
    else:
            print(" I don't know ")
