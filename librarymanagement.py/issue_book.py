from utils import book, issued_book
def issue_book():
    if len(book)==0:
        print("No books avb.")
    else:
        book_name=input("enter book name to issue").strip().upper()
        if book_name in book:
            book.remove(book_name)
            issued_book.append(book_name)
            print(f"Book - {book_name} issued successfully")
        else:
            print("no such book avb.!!!")

