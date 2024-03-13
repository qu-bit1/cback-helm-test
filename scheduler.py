import time
import random
import datetime
from db import delete_task, cursor, update_task

# execute_task function
def execute_task(task_id, name, execution_time, recurrence_type, recurrence_interval):
    print(f"Executing task '{name}' (ID: {task_id}) at {execution_time}...")
    time.sleep(random.randint(1, 5))
    print(f"Task '{name}' (ID: {task_id}) completed at {datetime.datetime.now()}")

# if recurring task calculate next_execution_time to update in db
def calculate_next_execution_time(execution_time, recurrence_type, recurrence_interval):
    execution_time = datetime.datetime.strptime(execution_time, '%Y-%m-%d %H:%M:%S')
    # Calculate next execution time based on recurrence type
    if recurrence_type == 'daily':
        next_execution_time = execution_time + datetime.timedelta(days=recurrence_interval)
    elif recurrence_type == 'weekly':
        next_execution_time = execution_time + datetime.timedelta(weeks=recurrence_interval)
    elif recurrence_type == 'monthly':
        next_execution_time = execution_time.replace(day=1)  # Start from the first day of the month
        next_execution_time += datetime.timedelta(days=30 * recurrence_interval)  # Approximation for months
        next_execution_time = next_execution_time.replace(day=min(next_execution_time.day, 28))  # Adjust for month end
    else:
        raise ValueError("Unsupported recurrence type")

    return next_execution_time.strftime('%Y-%m-%d %H:%M:%S')

def run_scheduler():
    while True:
        current_time = datetime.datetime.now()
        # print(f"Scheduler running at {current_time}...")
        cursor.execute("SELECT id, name, execution_time, recurrence_type, recurrence_interval FROM tasks WHERE execution_time <= ?", (current_time,))
        tasks_to_execute = cursor.fetchall()
        for task in tasks_to_execute:
            task_id, name, execution_time, recurrence_type, recurrence_interval = task
            execute_task(task_id, name, execution_time, recurrence_type, recurrence_interval)
            # if recurring task update in db else delete after executing
            if recurrence_type and recurrence_interval:
                update_task(task_id, name, calculate_next_execution_time(execution_time, recurrence_type, recurrence_interval))
            else:
                delete_task(task_id)
        time.sleep(1)

print("running scheduler")
run_scheduler()
