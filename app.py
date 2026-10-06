import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'todos.db')


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()


@app.route('/')
def index():
    with get_db_connection() as conn:
        todos = conn.execute(
            'SELECT * FROM todos ORDER BY completed ASC, id DESC'
        ).fetchall()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title', '').strip()
    if title:
        with get_db_connection() as conn:
            conn.execute('INSERT INTO todos (title) VALUES (?)', (title,))
            conn.commit()
    return redirect(url_for('index'))


@app.route('/toggle/<int:todo_id>', methods=['POST'])
def toggle(todo_id):
    with get_db_connection() as conn:
        conn.execute(
            'UPDATE todos SET completed = 1 - completed WHERE id = ?',
            (todo_id,)
        )
        conn.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    title = request.form.get('title', '').strip()
    if title:
        with get_db_connection() as conn:
            conn.execute(
                'UPDATE todos SET title = ? WHERE id = ?',
                (title, todo_id)
            )
            conn.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete(todo_id):
    with get_db_connection() as conn:
        conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
        conn.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    print("Starting Flask TODO App at http://127.0.0.1:5000 ...")
    app.run(debug=True)
