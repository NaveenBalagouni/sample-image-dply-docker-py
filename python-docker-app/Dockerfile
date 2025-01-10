# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt first to install dependencies
COPY requirements.txt ./

# Install specific compatible versions of Flask and Werkzeug
RUN pip install --no-cache-dir Flask==2.0.3 Werkzeug==2.0.3

# Install other dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
