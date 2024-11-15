# Virtual Book Club

Welcome to the Virtual Book Club! This web application allows users to create and join book clubs, explore books, and engage in a community of book lovers.

---

## Features

- **Book Clubs**: Create, edit, delete, and view book clubs.
- **Books**: Add, update, delete, and browse books.
- **User-Friendly Design**: Aesthetic and responsive interface built with Bootstrap.
- **Hosted Online**: Access the project via (https://bookclub-lucc.onrender.com/)(#) (replace `#` with the actual link).

---

## Navigation Guide

### Home Page
- **Description**: The landing page introduces the Virtual Book Club.
- **Features**: Provides buttons to navigate to book clubs and books.
- **URL**: `/`

### Book Clubs
- **Description**: View the list of all book clubs with options to create, edit, or delete clubs.
- **Features**:
  - View clubs in a table format.
  - Buttons for "Edit" and "Delete" actions.
  - "Create New Club" button.
- **URL**: `/clubs/`

#### Add/Edit Club
- **Description**: Add a new club or edit an existing one.
- **Features**:
  - Form to input club details.
  - "Save" button to submit changes.
- **URLs**:
  - Create: `/clubs/create/`
  - Edit: `/clubs/<club_id>/edit/`

#### Delete Club
- **Description**: Confirm deletion of a club.
- **URL**: `/clubs/<club_id>/delete/`

### Books
- **Description**: View the list of all books with options to add, update, or delete books.
- **Features**:
  - Books displayed in a card layout.
  - Buttons for "Edit" and "Delete" actions.
  - "Add New Book" button.
- **URL**: `/books/`

#### Add/Edit Book
- **Description**: Add a new book or edit an existing one.
- **Features**:
  - Form to input book details (Title, Author, Genre, Summary).
  - "Save" button to submit changes.
- **URLs**:
  - Create: `/books/create/`
  - Edit: `/books/<book_id>/edit/`

#### Delete Book
- **Description**: Confirm deletion of a book.
- **URL**: `/books/<book_id>/delete/`

---

