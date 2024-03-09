A task scheduler in python that interacts with the sqlite3 database. The service allows users to schedule tasks to be executed at a specified time.

### How to run:
Run `main.py` preferably in two terminals. You'll have the following 6 options:
```
1. Create Task
2. Read Tasks
3. Update Task
4. Delete Task
5. Run Scheduler
6. Exit
```
Use one terminal to query the db i.e create, read etc. and one to run scheduler constantly.
### Specifications:
- Each task have a unique id, name, and scheduled execution time.
- Supports CRUD operations
- Execute tasks at their scheduled times (i.e sleeps for a random amount of time from 1 to 5 seconds to simulate work)
### File structure:
- `db.py` - Basic db queries like create, update etc.
- `scheduler.py` - Functions to run scheduler
- `main.py` - Shows menu, main file to run and interact with the service