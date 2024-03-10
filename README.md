## README

1. A task scheduler in python that interacts with the sqlite3 database. The service allows users to schedule tasks to be executed at a specified time.

### How to run:
#### With RESTful API:
1. Create a virtual environment and install flask by `pip install flask`
2. Run app.py.
3. Use Postman or CURL to test, e.g for POST
```
curl -X POST \
  http://127.0.0.1:5000/tasks \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Task 1",
    "execution_time": "2024-03-10 10:00:00",
    "recurrence_type": "daily",
    "recurrence_interval": 1
  }'
```
To GET
```
curl -X GET http://127.0.0.1:5000/tasks
```
For updating and deleting specify the task id after the link like `http://127.0.0.1:5000/tasks/1` and use `PUT` , `DELETE` requests.

#### Without RESTful API:
Run `main.py` to do CRUD ops and `scheduler.py` simultaneously.

`main.py` will greet you with the following options.
```
1. Create Task
2. Read Tasks
3. Update Task
4. Delete Task
5. Exit
```
Use one terminal to query the db i.e create, read etc. and one to run scheduler constantly.

### Specifications:
- Each task have a unique id, name, and scheduled execution time.
- Supports CRUD operations
- Execute tasks at their scheduled times (i.e sleeps for a random amount of time from 1 to 5 seconds to simulate work)
- Recurring task functionality

### File structure:
- `app.py` - Flask server to implement a RESTful API for interacting with the service
- `db.py` - Basic db queries like create, update etc.
- `scheduler.py` - To run scheduler also handles the recurring logics
- `main.py` - Shows menu, main file to run and interact through CRUD ops with the service

---

2. Dockerizing:
- `app.Dockerfile` - Dockerfile to build a docker image for the flask server
- `scheduler.Dockerfile` - Dockerfile to build a docker image for the scheduler
- `docker-compose.yml` - Docker compose file to run both the images

#### How to run:
This will build & start both the containers(you'll see the output of the flask server), I have defined ports to be 8080:5000 . If facing problems please change those in `docker-compose.yml`.
```
docker compose up
```

For CRUD ops see the following examples:
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Task 1", "execution_time": "2024-03-10 20:00:00"}' http://localhost:8080/tasks

curl -X POST -H "Content-Type: application/json" -d '{"name": "Task 2", "execution_time": "2024-03-10 21:00:00", "recurrence_type": "weekly", "recurrence_interval": 1}' http://localhost:8080/tasks

curl -X GET http://localhost:8080/tasks

curl -X GET http://localhost:8080/tasks/1
```


