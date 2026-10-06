# Flask & SQLite Minimal CRUD TODO App

A clean, modern, single-page CRUD TODO application built with **Flask**, **SQLite**, and vanilla CSS.

---

## Project Structure

```text
flask-todo-app/
├── app.py                # Main Flask backend with SQLite operations
├── requirements.txt      # Dependency list (Flask)
├── static/
│   └── style.css         # Modern dark glassmorphic styling
└── templates/
    └── index.html        # Responsive frontend template with inline editing
```

---

## Features (CRUD)

- **Create**: Add new tasks with the input field.
- **Read**: View active and completed tasks ordered by state and recency.
- **Update**:
  - Click checkbox to toggle task status between complete / pending.
  - Click the **✎** edit button to rename tasks inline.
- **Delete**: Remove tasks with the **✕** button.
- **Persistent Storage**: Uses standard SQLite database (`todos.db`) created automatically on first run.

---

## How to Run

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/Eng-Munya/flask-todo-app.git
   cd flask-todo-app
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Start the application:
   ```powershell
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
