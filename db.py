import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# init db
def initialize_database():
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, name TEXT, execution_time TIMESTAMP,
                 recurrence_type TEXT, recurrence_interval INTEGER)''')
# create task
def create_task(name, execution_time, recurrence_type=None, recurrence_interval=None):
    cursor.execute("INSERT INTO tasks (name, execution_time, recurrence_type, recurrence_interval) VALUES (?, ?, ?, ?)",
                   (name, execution_time, recurrence_type, recurrence_interval))
    conn.commit()

# read tasks
def read_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

#update task
def update_task(task_id, new_name, new_execution_time):
    cursor.execute("UPDATE tasks SET name = ?, execution_time = ? WHERE id = ?", (new_name, new_execution_time, task_id))
    conn.commit()

#delete task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

def close_connection():
    conn.close()
