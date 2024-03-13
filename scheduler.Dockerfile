FROM python:3.9-slim

WORKDIR /app

COPY . .
# CMD ["python", "scheduler.py"]
CMD ["bash", "-c", "while [ ! -f tasks.db ]; do sleep 1; done && python scheduler.py"] # only run when db is initialised
