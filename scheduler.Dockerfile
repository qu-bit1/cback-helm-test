# Use the official Python image as base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the source code into the container
COPY . .

# Command to run the scheduler script
CMD ["python", "scheduler.py"]
