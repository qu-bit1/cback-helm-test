import time
import random
from datetime import datetime
from db import delete_task, cursor

def execute_task(task_id, name, execution_time):
    print(f"Executing task '{name}' (ID: {task_id}) at {execution_time}...")
    time.sleep(random.randint(1, 5))
    print(f"Task '{name}' (ID: {task_id}) completed at {datetime.now()}")


def run_scheduler():
    while True:
        current_time = datetime.now()
        cursor.execute("SELECT * FROM tasks WHERE execution_time <= ?", (current_time,))
        tasks_to_execute = cursor.fetchall()
        for task in tasks_to_execute:
            task_id, name, execution_time = task
            execute_task(task_id, name, execution_time)
            delete_task(task_id)
        time.sleep(1)