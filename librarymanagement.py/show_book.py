from utils import book
def show_book():
    if len(book)==0:
        print("no book avb.")
    else:
        print("avb. book")
        for _ in book:
            print(_)