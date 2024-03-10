from flask import Flask, request, jsonify, g
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'tasks.db'

"""
SQLite objects are thread-local, meaning they can only be used within the same thread where they were created.
To execute all the db ops within the same thread where the SQLite connection and cursor were created in the flask application we use Flask's
g object, which provides a thread-local storage for storing data during the lifetime of a request.
"""
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def initialize_database():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                        (id INTEGER PRIMARY KEY, name TEXT, execution_time TIMESTAMP,
                        recurrence_type TEXT, recurrence_interval INTEGER)''')
        db.commit()

def create_task(name, execution_time, recurrence_type=None, recurrence_interval=None):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (name, execution_time, recurrence_type, recurrence_interval) VALUES (?, ?, ?, ?)",
                   (name, execution_time, recurrence_type, recurrence_interval))
    db.commit()

def read_tasks():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def update_task(task_id, new_name, new_execution_time):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE tasks SET name = ?, execution_time = ? WHERE id = ?", (new_name, new_execution_time, task_id))
    db.commit()

def delete_task(task_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()

@app.route('/tasks', methods=['POST'])
def create_task_endpoint():
    data = request.json
    name = data.get('name')
    execution_time = data.get('execution_time')
    recurrence_type = data.get('recurrence_type')
    recurrence_interval = data.get('recurrence_interval')

    create_task(name, execution_time, recurrence_type, recurrence_interval)
    return jsonify({"message": "Task created successfully."}), 201

@app.route('/tasks', methods=['GET'])
def read_tasks_endpoint():
    tasks = read_tasks()
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task_endpoint(task_id):
    data = request.json
    new_name = data.get('name')
    new_execution_time = data.get('execution_time')

    update_task(task_id, new_name, new_execution_time)
    return jsonify({"message": "Task updated successfully."})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_endpoint(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted successfully."})

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
