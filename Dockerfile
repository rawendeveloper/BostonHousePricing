# Use the official Python 3.7 image as the base image
FROM python:3.7

# Set environment variables
# It's a good practice to set the PORT environment variable in the Dockerfile
# You can define a default value that can be overridden at runtime
ENV PORT=8000

# Copy the current directory contents into the /app directory in the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE $PORT

# Command to run the application using Gunicorn
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:$PORT", "app:app"]
