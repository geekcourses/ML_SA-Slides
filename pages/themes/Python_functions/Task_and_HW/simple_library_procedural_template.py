def add_book(isbn, title, author, status='available', borrower=None):
    """ Add new book to the library.
        A book cannot be added if another book with the same ISBN already exists in the library.
    Args:
        isbn: The ISBN of the book
        title: The title of the book
        author: The author of the book
        status: The status of the book (available or borrowed)
        borrower: The name of the borrower

    Returns:
        None
    """
    ### YOUR CODE HERE

def borrow_book(isbn, borrower):
    """ Borrow a book from the library.
    Args:
        isbn: The ISBN of the book
        borrower: The name of the borrower
    Returns:
        None
    """
    ### YOUR CODE HERE

def return_book(isbn):
    """ Return a book to the library.

    Args:
        isbn: The ISBN of the book

    Returns:
        None
    """
    ### YOUR CODE HERE

def list_books():
    """ List all books in the library

    Args:
        None

    Returns:
        None
    """
    ### YOUR CODE HERE

### TEST:
if __name__=="__main__":
    # the Library Data Structure
    library = []

    add_book(1111,"Python Programming", "Jon Doe")
    add_book(2222, "Learning AI", "Jane Smith")
    borrow_book(1111, 'Ivan')
    borrow_book(1111, 'Stoyan')
    list_books()

### Expected output:
# Python Programming has been added to the library.
# Learning AI has been added to the library.
# Python Programming has been borrowed by Ivan
# Book with ISBN: 1111 is not available in the library.
# ISBN: 1111, Title: Python Programming, Author: Jon Doe, Status: borrowed, Borrower: Ivan
# ISBN: 2222, Title: Learning AI, Author: Jane Smith, Status: available, Borrower: None


