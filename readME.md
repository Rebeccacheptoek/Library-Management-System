
# Library Management System

The Library System is a web-based application that manages a library's collection of books, members, and transactions. It provides features such as book search, book borrowing, member management, and transaction tracking.

## Features

- Book Management: Add, edit, and delete books from the library collection. Each book contains information such as title, author, genre, and quantity.
- Member Management: Add, edit, and delete library members. Each member has details such as name, contact information, and borrowing history.
- Book Search: Search for books by title, author to find specific books in the library.
- Book Borrowing: Allow members to borrow books from the library. Track the borrowing history, due dates, and return status of each book.
- Transaction Tracking: Keep a record of all book transactions, including borrowing and returning books.


## Screenshots

### Register
![Register](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/register.png)
*Screenshot of the Register page where users can create a new account.*

### Login
![Login](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/login.png)
*Screenshot of the Login page where users can sign in to their account.*

### Books
![Books](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/books.png)
*Screenshot of the Books page showing the list of available books in the library.*

### Members
![Members](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/members.png)
*Screenshot of the Members page displaying the list of registered library members.*

### Issue Book Form
![Issue Book Form](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/issue_book_form.png)
*Screenshot of the Issue Book Form where librarians can process book borrowing for a member.*

### Returned Books
![Returned Books](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/returned_books.png)
*Screenshot of the Returned Books page showing the list of books returned by members.*

### Books Issued
![Books Issued](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/books_issued.png)
*Screenshot of the Books Issued page displaying the list of books currently issued to members.*

### Reports
![Reports](https://github.com/Rebeccacheptoek/Library-Management-System/blob/main/screenshots/reports.png)
*Screenshot of the Reports page providing graphical reports and insights about the library system.*

## Installation

1. Clone the repository: `git clone https://github.com/your-username/library-system.git`
2. Navigate to the project directory: `cd library-system`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Access the application at `http://localhost:8000` in your web browser.

## Technologies Used

- Django: Python web framework for building the backend of the application.
- HTML/CSS: Frontend markup and styling.
- JavaScript: Used for interactivity and client-side validation.
- MySQL: Database management system for storing books, members, and transactions.

## Contributing

Contributions to the Library System are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.

