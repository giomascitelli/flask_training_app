# Flask Book API

A simple Flask application for managing books.

## Installation

1. Create a virtual environment:
    ```
    python -m venv venv
    ```
2. Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```
        source venv/bin/activate
        ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Initialize the database:
    ```
    flask init-db
    ```

## Running the Application

Start the Flask development server:

    ```
    python run.py
    ```

## API Endpoints

- `GET /books` - Retrieve all books
- `POST /books` - Add a new book
- `GET /book/<id>` - Retrieve a book by ID
- `PUT /book/<id>` - Update a book by ID
- `DELETE /book/<id>` - Delete a book by ID

