from flask import Blueprint, request, jsonify
from .database import get_db

bp = Blueprint('main', __name__)

@bp.route('/books', methods=['GET', 'POST'])
def multiple_books():
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('SELECT * FROM book')
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=row[3])
            for row in cursor.fetchall()
        ]
        return jsonify(books)

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']

        sql = 'INSERT INTO book (author, language, title) VALUES (?, ?, ?)'
        cursor.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        return f"Book with the id: {cursor.lastrowid} created successfully", 201

@bp.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id = ?", (id,))
        book = cursor.fetchone()
        if book:
            return jsonify(book), 200
        else:
            return "Something went wrong", 404

    if request.method == 'PUT':
        sql = '''UPDATE book SET author = ?, language = ?, title = ? WHERE id = ?'''
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']

        updated_book = {'id': id, 'author': author, 'language': language, 'title': title}

        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(updated_book)

    if request.method == 'DELETE':
        cursor.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
        return f"The book with id: {id} has been deleted.", 200

