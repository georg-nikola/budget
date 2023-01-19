# Use the official Django image as the base image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# copy only the requirements file
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# copy the rest of the files
COPY ./budget/ /budget

# Expose the port 8000
EXPOSE 8000
