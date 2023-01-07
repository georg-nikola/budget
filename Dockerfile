FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app
COPY ./budget/ /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port 8000
EXPOSE 8000

# Run the command to start the Django development server
CMD ["python", "manage.py", "collectstatic ", "--no-input"]
